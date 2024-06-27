from flask import render_template, url_for, flash, redirect, request
#flash is for mesages uppon registration
#redirect is for redirecting users uppong logging 
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post
from flaskblog import app, db, bcrypt
from flask_login import login_user, current_user, logout_user, login_required # to manage login logout and when the login is mandatory login_required 
posts = [
    {

    'author' : 'Moad elhanbout',
    'title' : 'Test post',
    'date_posted' : '20, may, 2024',
    'content' : 'This is my first post on this blog'
},
    {

    'author' : 'moad elhanbout',
    'title' : 'Test post number 2',
    'date_posted' : '21, may, 2024',
    'content' : 'this is my second post on this blog'
}

]
@app.route("/")
def home():
    return render_template("home.html", posts=posts)

@app.route("/about")
def about():
    return render_template("about.html", title="about")

@app.route("/register", methods=['GET', 'POST']) #we add methodes to accept get and post requet when ubmitting a form
def register():
    if current_user.is_authenticated: #if the user is alreadt signed in it doesn't have to login again
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8') #this is to hash password
        user = User(username=form.username.data, email=form.email.data, password=hashed_password) #create the user 
        db.session.add(user)#add user to db 
        db.session.commit()#commit the changes to the db
        flash(f"Your account has been created! and you're able to log in now", "success")
        return redirect(url_for("login"))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else (url_for('home'))#if we type a link to account and asks to og in first after login will continue to account
        else:
            flash("Login failed. Please check Email or password ", 'danger') #danger is boot start class for allert 
    return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/account")
@login_required
def account():
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('account.html', title='Account', image_file=image_file)