from flask import Flask, render_template, request, redirect, url_for
from flask.helpers import flash
from flask.wrappers import Request
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)
app.secret_key = "anjaysecret"

app.config['MYSQL_DATABASE_USER'] = 'humai'
app.config['MYSQL_DATABASE_PASSWORD'] = '123'
app.config['MYSQL_DATABASE_DB'] = 'untold'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

def Convert(a):
    it = iter(a)
    res_dct = dict(zip(it, it))
    return res_dct

def query_db(query, args=(), one=False):
    conn = mysql.connect()
    cur = conn.cursor()
    try:
        cur.execute(query, args)
        conn.commit()
        r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
        result = (r[0] if r else None) if one else r
        return result if result else None
    except Exception as e:
        print("Database Error: ", e)
    finally:
        cur.close()
        conn.close()

@app.route("/", methods=['GET', 'POST'])
def index():
    query_read = query_db("select * from story order by created_at desc")
    return render_template("index.html", story=query_read)

@app.route('/confess', methods=['GET','POST'])
def confess():
    title_story = request.form['title_story']
    username = request.form['username']
    stories = request.form['stories']
    query_create = query_db("insert into story(title_story, username, stories) values (%s, %s, %s)", (title_story, username, stories))
    return redirect(url_for('index'))

@app.route('/result', methods=['GET', 'POST'])
def result():
    if request.method == "GET":
        query = request.args['cari']
        query_search = query_db("select * from story where concat(title_story, stories, username) like %s ", ("%" + query + "%"))
        anu = tuple(query_search)
        return render_template("result.html", data=anu)
    return redirect(url_for("index"))
        