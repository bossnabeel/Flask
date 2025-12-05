from flask import Blueprint,jsonify
auth_bp = Blueprint('auth', __name__, url_prefix='/auth')
public_bp = Blueprint('public', __name__)

@auth_bp.route('/login')
def login():
    return "Login"
@auth_bp.route('/register')
def register():
    return "Public Register"


@public_bp.route('/login')
def login():
    return "Login"
@public_bp.route('/register')
def register():
    return "Public Register"
