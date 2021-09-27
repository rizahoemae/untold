# Untold - The Safe World

Seseorang mungkin memiliki cerita, tetapi tidak bisa diceritakan ke orang lain. Bisa jadi karena tidak memiliki teman yang dapat dipercayai, atau mungkin mereka adalah tipikal orang yang tidak suka cerita ke siapa saja. Pada awalnya, mungkin make sense untuk memendam perasaan sendiri. Tapi jika sudah lama, pasti mereka membutuhkan tempat untuk menuang keluh kesah. Pasti mereka ingin didengar. Platform aman ini untuk mengungkapkan the untold (yang tak pernah terbilang). Harapannya platform ini dapat menjadikan tempat terbaik untuk mereka dalam menuangkan perasaan dengan anonymous. 

Untold di sini menggunakan logika CR (create dan read). Menggunakan teknologi ```Flask Python, Tailwind CSS,``` dan ```MySQL```. 

## Getting started
Dibawah ini adalah langkah-langkah untuk me-run Untold. Harap baca satu-satu secara berurutan. Semoga dapat dikembangkan~~

### Prerequisite - setup MySQL
* db_name: untold
* db_host: localhost 
* db_user: ur_user
* db_pass: 'ur_pass'

#### Create Database 
```create database untold;```

#### Create Table 
```
use untold;

create table story (
id_story int(11) not null primary key auto_increment, 
title_story varchar(255) not null,
stories varchar(255) not null, 
created_at timestamp default current_timestamp on update current_timestamp,
username varchar(255) null default 'unknown');
```
atau yang nantinya bisa bikin table yang endingnya kek gini:
```
+-------------+--------------+------+-----+---------------------+-------------------------------+
| Field       | Type         | Null | Key | Default             | Extra                         |
+-------------+--------------+------+-----+---------------------+-------------------------------+
| id_story    | int(11)      | NO   | PRI | NULL                | auto_increment                |
| title_story | varchar(255) | NO   |     | NULL                |                               |
| stories     | varchar(255) | NO   |     | NULL                |                               |
| created_at  | timestamp    | NO   |     | current_timestamp() | on update current_timestamp() |
| username    | varchar(255) | YES  |     | unknown             |                               |
+-------------+--------------+------+-----+---------------------+-------------------------------+
```
atau bisa juga import langsung dari [untold.sql](https://github.com/rizahoemae/untold/blob/main/untold.sql)


#### Create user 
```create user ur_user@localhost identified by 'ur_pass';```


#### Grant user 
```grant all privileges on untold.* to ur_user@localhost identified by 'ur_pass';```

### Pull repo 
clone dan pull repo menggunakan [cara ini](https://stackoverflow.com/questions/1408790/how-do-i-pull-my-project-from-github) atau menggunakan alternatif zip file dan ekstrak sendiri.

### Prerequisite - install Flask
install Flask menggunakan ```pip install Flask```, install juga Flask MySQL dengan ```pip install Flask-MySQL```

### Setup [route.py](https://github.com/rizahoemae/untold/blob/main/route.py)
sesuaikan baris-baris ini dengan punya kamu~
```
app.config['MYSQL_DATABASE_USER'] = 'ur_user' 
app.config['MYSQL_DATABASE_PASSWORD'] = 'ur_pass' 
app.config['MYSQL_DATABASE_DB'] = 'untold' 
app.config['MYSQL_DATABASE_HOST'] = 'localhost' 
```
### Setup venv
* masuk pada folder untold: ```cd untold```
* buat venv dengan: ```python3 -m venv venv``` atau menggunakan existing python version punya kamu~~
* jika belum punya venv python, install dengan: ```sudo apt-get install python3-venv``` (berlaku untuk linux, windows menyesuaikan kwkwk)
* aktifkan venv yang telah dibuat tadi dengan: ```source venv/bin/activate``` atau bisa juga pake ```. venv/bin/activate```
* run dis things: ```export FLASK_APP=route``` dan ```flask run```

### Done. 
biasanya setelah venv dinyalakan, web server juga ikut jalan. terus tinggal buka deh di localhost:5000

## Preview singkat untold
![image](https://user-images.githubusercontent.com/55048401/134859019-1792f410-83b9-465d-8ebc-88230058280a.png)
yahh mana ada bug segala. intinya kek [gini](https://rizahoemae.notion.site/Showcase-3f598fede0cc45789a2dd3c01d3dee12#:~:text=visit%20my%20Instagram-,User%20Interface,-In%20short%2C%20untold) 
