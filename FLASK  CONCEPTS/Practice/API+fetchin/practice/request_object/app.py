from flask import Flask, render_template,request
app=Flask(__name__) 
@app.route("/results")
def args():
    #for using like searching queyr etc
    p=request.args.get("search_query")
    return f"Seached {p}"
#form.get s
@app.route("/form", methods=['POST','GET'])
def form():
    if request.method=="POST":
        name=request.form.get('name')
        password=request.form.get('password')
        return f' Name: {name} Password: {password}'  
        
    return ''' <form action='/form' method='POST' >
                    <input id='name' name='name' type='text'><br>
                    <input id='password'name='password' type='text'>
                    <button type='submit'> login</button>
                </form>
'''
app.run(port=3500)
