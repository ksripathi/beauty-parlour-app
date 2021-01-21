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
    return 'Welcome to beauty parlour website'


@app.route('/beauty-parlour-list')
def list():
    # Mysql implemation takes place
    return 'List of bueatt-parlours'

@app.route('/add-beauty-parlour')
def add():
    # Mysql implemation takes place
    return 'add beauty parlour data'

app.run(host='0.0.0.0', port=81)
