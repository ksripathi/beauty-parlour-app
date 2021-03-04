'''
sample application
'''
from flask import Flask, render_template, request,redirect
from flask_mysqldb import MySQL
app = Flask(__name__)
app.config['MYSQL_HOST'] = 'beautyparlour-db.cjbzogxmg5tz.us-east-2.rds.amazonaws.com'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'beauty123'
app.config['MYSQL_DB'] = 'sripathi'

mysql = MySQL(app)
@app.route('/')
def index():
    '''
    Main landing api
    '''
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM Studio7beautyparlor')
    data = cur.fetchall()
    return render_template('list.html', output_data = data)

@app.route('/add-beauty-parlour', methods=['GET','POST'])
def add():
    '''
    API for adding details
    '''
    if request.method == "GET":
        return render_template('index.html')
    if request.method == "POST":
        details = request.form
        name = details['name']
        age = details['age']
        sex = details['sex']
        location = details['location']
        contact = int(details['contact'])
        email = details['email']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO Studio7beautyparlor(name, age, sex, location, contact, email) " +\
                    "VALUES (%s, %s, %s, %s, %s, %s)", \
                    (name, age, sex, location, contact, email))
        mysql.connection.commit()
        cur.close()
    return redirect("/")

app.run(host='0.0.0.0', port=8081, debug="true")
