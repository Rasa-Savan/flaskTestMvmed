# user_models.py
import uuid

from werkzeug.security import generate_password_hash, check_password_hash
from extensions import db


class User(db.Model):
    """
    user model which mapped to database:
    table_name: users
    columns:
        id, username, email, password
    """
    __tablename__ = 'users'
    id = db.Column(db.String(), primary_key=True, default=str(uuid.uuid4()))
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def set_password(self, password):
        """Method of hashing password before save to db during register new user"""
        self.password = generate_password_hash(password)

    def check_password(self, password):
        """Method of comparison hashing password during login with existing password"""
        return check_password_hash(self.password, password)

    def save(self):
        """Method of saving user object into database"""
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_existing_username_email(cls, username, email):
        """
        Method of verification existing username and email in database
        :return: boolean
            True: means a username or password exist
            False: means a username or password does not exist
        """
        return cls.query.filter_by(username=username).first() or User.query.filter_by(
            email=email).first()
