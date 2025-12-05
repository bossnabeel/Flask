from flask import Flask, render_template,request as req,jsonify
app=Flask(__name__) 
secret_key="jldjf09fio-l@#(ljl9e(#NM>ip0LO0+546464p098uuhgko0-9huijiunjunbh@#$^&^E))"

@app.route("/get_info", methods=['POST','GET'])
def info():
    if req.method=='POST':
        
        name=req.form.get('name')
        age=req.form.get('age')
        
        if not name or not age:
            return jsonify({ "error": "Missing parameters" })
        else :
            return f"Hello {name}, your age is {age}"

    return render_template('index.html')


@app.route('/submit_form', methods=['POST','GET'])
def index():
    
    if req.method=='POST':
        
        data=req.get_json()
        username=data.get('username')
        email=data.get('email')
        password=data.get('password')
        
        if not email or not password or not username:
            
            return jsonify({ "error": "Missing fields🔥" })
        else:
            return "Form received successfully!"
        
    return render_template('login.html')


@app.route('/json_test', methods=['POST','GET'])
def api():
    if req.method=="POST":
        message=req.get_json()
        header=req.headers.get('auth-key')
        auth=header['auth-key']
        if auth==secret_key:
            return f"Authorized {message}"
        else:
             return f"UnAthotized",401
         
if __name__=="__main__":
    app.run()