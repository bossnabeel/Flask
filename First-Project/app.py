import mysql.connector
from flask_cors import CORS
from flask import Flask, request,session
from flask import jsonify, redirect,url_for
from flask import render_template
app=Flask(__name__)
CORS(app)
app.secret_key='9j0j08n8--i778t8-3j@#$%^68tboolk'
class MYSQL_auth():
    def __init__(self,host='127.0.0.1',username='root',password='9090',port=3306, database='USERS'):
        self.conn=mysql.connector.connect(
            host=host,
            user=username,
            password=password,
            port=port,
            database=database
        )
        self.cursor=self.conn.cursor(dictionary=True)
        
    def check_user(self,username,password):
        try:
            query='select *from `AUTH` where username=%s and password=%s'
            self.cursor.execute(query,(username,password))
            user=self.cursor.fetchone()
            if user:
                return 1
        except:
            return 0
    
    def add_user(self,name,lname,username,email,password):
        try:
            query='select username, email from `AUTH` where username=%s or email=%s'
            self.cursor.execute(query,(username,email))
            user=self.cursor.fetchone()
            if user:
                return "present"
            query='INSERT INTO `AUTH`(name,lname,username,email,password) values(%s,%s,%s,%s,%s)'
            self.cursor.execute(query,(name,lname,username,email,password))
            self.conn.commit()
            return 1
        except:
            return 0;
        
    def close_conn(self):
        self.cursor.close() 
        self.conn.close()
        print('close done')
        
    def update_password(self, newpassword,username,password):
        try:
            query='Update  AUTH set password=%s where username=%s and password=%s'
            self.cursor.execute(query,(newpassword,username,password))
            self.conn.commit()
            return 1
        except:
            return 0
    
    def update_username(self, newusername,username,password):
        try:
            query='Update  AUTH set username=%s where username=%s and password=%s'
            self.cursor.execute(query,(newusername,username,password))
            self.conn.commit()
            return 1
        except Exception as e:
            return jsonify({e})
@app.route("/login",methods=['POST','GET'])
def login():
    if 'username'in session:
        return redirect(url_for('home'))
    if request.method=='POST':
        data=request.get_json()
        username=data.get('username')
        password=data.get('password')
        db=MYSQL_auth()
        if db.check_user(username,password):
            db.close_conn()
            session['username']=username
            return jsonify({"success":True, "message":"user found"}),200
        else:
            db.close_conn()
            return jsonify({"success":False,"message":"unauthorized"}),402
    return render_template('login.html')
@app.route('/register',methods=['POST','GET'])
def register():
    if 'username' in session:
        return redirect(url_for('home'))
    if request.method=='POST':
        data=request.get_json()
        name=data.get('name')
        lname=data.get('lname')
        username=data.get('username')
        email=data.get('email')
        password=data.get('password')
        db=MYSQL_auth()
        conn=db.add_user(name,lname,username,email,password)
        if conn:
            if conn=='present':
                return jsonify({"success":False,"message":"User exist Already"})
            else:
                return jsonify({"success":True,"message":"login SUcces"}),200
        else:
            return jsonify({"success":False,"message":"please try again server is busy"}),429
    return render_template('register.html')
@app.route("/")
def home():
    if 'username' not in session:
        return redirect(url_for("login"))
    return render_template("index.html")
@app.route('/logout')
def logout():
    session.pop('username',None)
    return redirect(url_for('login'))
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
