from flask import render_template,redirect,url_for,abort
from . import main
from .forms import UpdateProfile,CommentForm,PostForm
from ..models import User,Post,Comment
from flask_login import login_required,current_user
from .. import db,photos
from ..request import get_quote
    
    # post = Post.query.all()


@main.route('/')
def index():
    title = 'Home - Welcome to The best Post Website Online'
    quote=get_quote()
    all_post = Post.get_all_post()
    return render_template('index.html', title = title, all_post=all_post,quote=quote)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)
        db.session.add(user)
        db.session.commit()
    return render_template("profile/profile.html", user = user)   

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.description = form.description.data

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)


@main.route('/new', methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()

    if form.validate_on_submit():
        post = form.post.data
        description = form.description.data
        new_post = Post(post =post , description = description)
        new_post.save_post()
        return redirect(url_for('.index'))
    return render_template('new_post.html', post_form=form)

@main.route('/comment/<int:id>',methods = ['GET','POST'])
@login_required
def new_comment(id):
    form = CommentForm()
    imishwi =Comment.query.filter_by(post_id = id).all()
    if form.validate_on_submit():
        comment = form.comment.data
        new_comment = Comment(comment = comment , post_id=id, user=current_user)
        new_comment.save_comment()
        return redirect(url_for('.new_comment',id=id))
    return render_template('new_comment.html', imishwi=imishwi,comment_form=form)