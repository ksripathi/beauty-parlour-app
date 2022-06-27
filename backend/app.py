'''
sample application
'''
from flask import Flask, render_template, request,redirect
app = Flask(__name__)

@app.route('/')
def index():
    '''
    Main landing api
    '''
    return render_template('list.html')

app.run(host='0.0.0.0', port=8081, debug="true")
