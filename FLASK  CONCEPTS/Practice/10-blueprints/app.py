from auth.routes import auth_bp,public_bp
from flask import Flask
app=Flask(__name__)
app.register_blueprint(auth_bp)
app.register_blueprint(public_bp)
if __name__=="__main__":
    app.run(debug=True)