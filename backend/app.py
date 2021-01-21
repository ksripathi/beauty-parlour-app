from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'sripathi'

mysql = MySQL(app)
@app.route('/')
def index():
    return 'Web App with Python Flask!'


@app.route('/beauty-parlour-list')
def list():
    dat
    return 'List of bueayt-parlours'

app.run(host='0.0.0.0', port=81)
