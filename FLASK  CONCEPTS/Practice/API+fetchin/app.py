from flask import Flask, render_template,session
from flask import redirect,url_for,jsonify,request 
app=Flask(__name__) 
app.secret_key="hlkhll$^&*(0-ln"
users={
    "nabeel":"1233"
}
@app.route("/",methods=["POST","GET"])
def login():
    if "user" in session:
        return redirect(url_for("home"))
    if request.method=="POST":
        data=request.get_json()
        username=data.get("username")
        password=data.get("password")
        if username in users and users[username]==password:
            session['user']=username
            return jsonify({ "success":True,"message":"Login Succesfull","user":username}),200
        elif not username in users or not users[username]==password:
            return jsonify ({ "success":False , "error": "Invalid username or password"}),401
    return render_template("login.html")
@app.route("/home", methods=["GET", "POST"])
def home():
    if not 'user'in session:
        return redirect(url_for('login'))
    return render_template("home.html")
@app.route("/logout", methods=["GET", "POST"])
def logout():
    session.pop("user",None)
    return redirect(url_for('login'))
if  __name__=="__main__" :
   app.run(debug=True)
