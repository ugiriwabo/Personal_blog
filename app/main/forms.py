from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,ValidationError
from wtforms.validators import Required,Email
from ..models import User,Post,Comment

class PostForm(FlaskForm):
    post=  TextAreaField('Post ', validators=[Required()])
    description = TextAreaField('description ', validators=[Required()])
    submit = SubmitField('Submit')
    

class CommentForm(FlaskForm):
    comment = TextAreaField('username comment', validators=[Required()])
    submit = SubmitField('Submit')




class UpdateProfile(FlaskForm):
    description = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')
