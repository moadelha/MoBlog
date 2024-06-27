from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
# pip install flask-sqlalchemy to work with db and can be used with diffrent dbs
from flask_login import LoginManager

from flask_bcrypt import Bcrypt


app = Flask(__name__)
app.config['SECRET_KEY'] = 'd9504692859a0e5b0c3badf5d6d9e2cb'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  #configure db
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_mesage_category = 'info'
from flaskblog import routs