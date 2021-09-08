from flask import Flask
from flaskext.mysql import MySQL

app = Flask(__name__)
app.config['SECRET_KEY'] = '5fa72358f0b4fb4f2c5d7de8c9a41846'
app.config['TEMPLATES_AUTO_RELOAD'] = True

app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_User'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'newsportal_db'

mysql = MySQL()
mysql.init_app(app)
