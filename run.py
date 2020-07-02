from flask import Flask,jsonify,redirect
from flask_cors import CORS
import json, os, signal
from flask import render_template,flash,redirect, url_for, request
from Model import db,User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_required, current_user


app=Flask(__name__)


@app.route('/api/',methods=['GET', 'POST', 'PUT','DELETE'])
def shutup():
    return redirect('/api/admin')

def create_app(config_filename):
    app.config.from_object(config_filename)
    from app import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')
    app.config['SECRET_KEY'] = '9OLWxND4o83j4K4iuopO'
    from Model import db
    db.init_app(app)
    return app


@app.route('/login/')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False
    user = User.query.filter_by(email=email).first()
    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return render_template('login.html')
    return render_template('profile.html', name=current_user.name,id=current_user.id)

@app.route('/signup/')
def signup():
    return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    user = User.query.filter_by(email=email).first()
    if user:
        flash('Email address already exists')
        return render_template('login.html')
    new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))
    db.session.add(new_user)
    db.session.commit()
    return render_template('profile.html', name=current_user.name,id=current_user.id)

@app.route('/logout/')
def logout():
    return 'Logout'

@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name,id=current_user.id)

@app.route('/',methods=['GET', 'POST', 'PUT','DELETE'])
def welcome():
    return "NOT HERE"

@app.route('/stopServer', methods=['GET'])
def stopServer():
    os.kill(os.getpid(), signal.SIGINT)
    return jsonify({ "success": True, "message": "Server is shutting down..." })


app = create_app("config")
CORS(app)

if __name__ == "__main__":
    app.run(debug=True)
