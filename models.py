from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from datetime import datetime
from sqlalchemy.ext.hybrid import hybrid_property
from database import db


convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

metadata = MetaData(naming_convention=convention)

# db = SQLAlchemy(metadata=metadata)

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    _password_hash = db.Column(db.String)
    image_url = db.Column(db.String)
    visits = db.relationship('Visit', backref='user', cascade='all')


    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'image_url': self.image_url
        }

    def __repr__(self):
        return f'<User {self.username}>'

    @hybrid_property
    def password(self):
        raise AttributeError('Cannot access password directly')

    @password.setter
    def password(self, new_pass):
        from app import bcrypt
        p_hash = bcrypt.generate_password_hash(new_pass.encode('utf-8'))
        self._password_hash = p_hash.decode('utf-8')

    def authenticate(self, password):
        from app import bcrypt
        return bcrypt.check_password_hash(self.password_hash, password.encode('utf-8'))

class Visit(db.Model):
    __tablename__ = "visits"
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    park_id = db.Column(db.Integer, db.ForeignKey('parks.id'), primary_key=True)
    visit_date = db.Column(db.DateTime, default=datetime.utcnow) 



class Park(db.Model):
    __tablename__ = "parks"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    location = db.Column(db.String)
    activities = db.Column(db.String)
    campgrounds = db.Column(db.String)
    videos = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    visits = db.relationship('Visit', backref='park', cascade='all')


    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name, 
            'location': self.location,
            'activities': self.activities,
            'campgrounds': self.campgrounds,
            'videos': self.videos
        }

    def __repr__(self):
        return f'<Park {self.name}>'
