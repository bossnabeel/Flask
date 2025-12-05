from flask import Flask,jsonify
import mysql.connector
app=Flask(__name__)
@app.route("/")
def home():
    return jsonify({ "message":"hello I am json file"})
@app.route("/<string:username>")
def index(username):
    connection=mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='9090',
        database='TESTED_DB',
        port=3306
    )
    cursor=connection.cursor(dictionary=True)
    cursor.execute('SELECT username,password from USERS WHERE username=%s',(username,))
    user=cursor.fetchone()
    cursor.close()
    connection.close()
    if user:
        return f"username :{user['username']} password::: {user['password']}"
    else:
        return "Not found User"
app.run()