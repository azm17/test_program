# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 17:56:33 2019

@author: Azumi Mamiya

pip3 install flask
"""
from flask import Flask,request, render_template
import my_function2 as my_func

app = Flask(__name__)
server_host='192.168.2.102'#this server host

SQLserver_host='192.168.2.107'#SQL server host
SQLserver_port=3306 #SQL server port
database_name='hydration_db' #database name

@app.route("/")
def entry():
    html = render_template('index.html')
    return html

@app.route("/hello", methods=["POST"])
def hello():
    usernid = request.form['user']
    userpass = request.form['pass']
    print("ID:{} LOGIN ".format(usernid),end='')
    try:
        hantei=my_func.kakunin(usernid,userpass,SQLserver_port,SQLserver_host,database_name)
    except:
        hantei=False
    print(hantei)
    if hantei:
        return render_template('hello.html', title='flask test', name=usernid)# lonin success
    else:
        return 'either id or pass is not match'# login fail

@app.route("/show", methods=["POST"])
def show():
    usernid = request.form['user']
    userpass = request.form['pass']
    print("ID:{} GET ".format(usernid),end='')
    try:
        data=my_func.sql_data_get(usernid,userpass,SQLserver_port,SQLserver_host,database_name)
        print(data)
        return 'OK'
    except:
        print('Fail')
        return 'NG'

if __name__ == "__main__":
    app.run(debug=False, host=server_host, port=50000)