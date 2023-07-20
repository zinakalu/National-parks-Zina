from flask import Flask, jsonify, make_response, request, session
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from database import db
# import os

# BASE_DIR = os.path.abspath(os.path.dirname(__file__))
# DATABASE = os.environ.get(
#     "DB_URI", f"sqlite:///{os.path.join(BASE_DIR, 'app.db')}")

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.json.compact = False
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///national-parks.db'  
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)
db.init_app(app)

migrate = Migrate(app, db)



bcrypt = Bcrypt(app)

# TBD
from models import User, Visit, Park


excluded_endpoints = ['signup', 'check_session', 'login', 'logout']

@app.before_request
def check_is_logged_in():
    if request.endpoint not in excluded_endpoints:
        user_id = session.get('user.id')
        user = User.query.filter(User.id == user_id).first()

        if not user:
            return {'error': 'User is not logged in'}, 401




@app.route('/')
def index():
    return '<h1>National Parks</h1>'

@app.get('/activities')
def get_all_activities():
    activities = Park.query.all()
    data = [activity.to_dict() for activity in activities]
    return make_response(
        jsonify(data), 200)

@app.get('/campgrounds')
def get_all_campgrounds():
    campgrounds = Park.query.all()
    data = [campground.to_dict() for campground in campgrounds]
    return make_response(jsonify(data), 200)

@app.route('/videos')
def get_all_videos():
    videos = Park.query.all()
    data = [video.to_dict() for video in videos]
    return make_response(jsonify(data), 200)

@app.post('/signup')
def signup():
    data = request.get_json()

    try:
        new_user = User(
            username=data.get('username'),
            image_url=data.get('image_url'),
            password=data.get('_password_hash')
        )

        new_user._password_hash = data.get('_password_hash')
        db.session.add(new_user)
        db.session.commit()

    except Exception as e:
        print(e)
        return {'error': 'Error creating user'}, 422


    return new_user.to_dict(), 201

@app.get('/check_session')
def check_session():
    user_id = session.get('user_id')
    user = User.query.filter(User.id == user_id).first()

    if not user:
        return {'error': 'User not logged in'}, 401
    return user.to_dict(), 200

@app.post('/login')
def login():
    data = request.get_json()

    user = User.query.filter(
        User.username == data.get('username')
    ).first()

    if not user or not user.authenticate(data.get('password')):
        return {'error': 'invalid login'}, 401

    session['user_id'] = user.id
    return user.to-dict(), 201

@app.delete('/logout')
def logout():
    user_id = session.pop('user.id')

    return {'message': 'Logout successful'}, 200


if __name__ == '__main__':
    app.run(port=5555, debug=True)