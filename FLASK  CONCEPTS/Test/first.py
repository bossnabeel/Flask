from flask import Flask, render_template,jsonify ,session,flash,get_flashed_messages
app=Flask(__name__)
app.secret_key="jklfjsklda"
@app.route("/")
def index():
    return """<h1>Hello nabeel</h1>"""
name="Nabeel"
@app.route("/user/<name>")
def user(name):
    return F"""hello {name} jii"""
@app.route("/data")
def data():
    return jsonify({"name":"Ali","age":20})
@app.route("/temp")
def temp():
    return render_template("index.html")
@app.route("/tp")
def _session():
    session['username']='sher'
    return f"{session['username']}"
@app.route("/flashed")
def Flash():
    flash("this is flashed")
    return f"""{get_flashed_messages()}"""
app.run(debug=True)

