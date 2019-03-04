from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
# from datetime import datetime 

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))  

class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    profile_pic_path = db.Column(db.String())
    password_hash = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))
    post=db.relationship('Post',backref='user',lazy='dynamic')
    comments=db.relationship('Comment',backref='user',lazy='dynamic')

    def __repr__(self):
        return f'User {self.name}'

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'User {self.username}'

    
class Post(db.Model):
    __tablename__ = 'post'

    id = db.Column(db.Integer,primary_key = True)
    post = db.Column(db.String)
    category = db.Column(db.Integer)
    description = db.Column(db.String(255))
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    comments = db.relationship('Comment',backref = 'post',lazy="dynamic")

    def save_post(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_all_post(cls):
        
        return Post.query.all()
    
    
class Comment(db.Model):
    __tablename__ = 'comment'

    id = db.Column(db.Integer,primary_key = True)
    comment = db.Column(db.String(255))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    post_id = db.Column(db.Integer,db.ForeignKey('post.id'))


    def __repr__(self):
        return f'User {self.name}'
    
    def save_comment(self):
            db.session.add(self)
            db.session.commit()
   
    @classmethod
    def get_all_comments(cls):
        return comment.query.all

class Profile(db.Model):
    
    __tablename__ ='post_profile'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255))

    def save_profile(self):
        
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_all_profile(cls):
        
        return Post.query.all()

class Quote:
    def __init__(self,id,author,quote):
        self.id =id
        self.author = author
        self.quote = quote

class Subscribe(db.Model):
    __tablename__ = 'subscribers'
    id = db.Column(db.Integer,primary_key = True)
    email = db.Column(db.String(255),unique = True,index = True)
    def __repr__(self):
        return f'User {self.email}'