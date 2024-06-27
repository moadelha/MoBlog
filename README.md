setting up the virtual env:
python3 -m venv venv
activate the virtual env by 
source venv/bin/activate



Create the db:
>>> from flaskblog import app, db
>>> app.app_context().push()
>>> db.create_all()

cretate a user using the console
>>> from flaskblog import app, db
>>> user_1 = User(username='Moad', email='moad3435@gmail.com', password='password')

Add user to db
>>> db.session.add(user_1)
Commit the added users to db
>>> db.session.commit()

View all users
>>> User.query.all()

delete all data:
db.drop_all()

to encrypt password in the db we use the dlask tool bcrypt 
to install it we do pip install flask-bcrypt
Example:
>>> from flask_bcrypt import Bcrypt
>>> bcrypt = Bcrypt()
>>> bcrypt.generate_password_hash('testing')
b'$2b$12$sjl5Ak0mnEawydrOmb6gGe3xeHt.A/s6ifgOZqY1f1wnmD22O2itq'
to remove the b at the start we user utf-8:
>>> bcrypt.generate_password_hash('testing').decode('utf-8')
'$2b$12$QntvpzC2cbWNpouKkrhRk.KUi28QRgFaCPnEs3IlG3VRHAa/S86tW'

everytime we rung the command above we get a new hash 
when we check hash against password we get True
>>> pass_wd = bcrypt.generate_password_hash('testing').decode('utf-8')
>>> bcrypt.check_password_hash("pass_wd", "testing")

________________________________________________________
we can use flask login to manage login to sessions 
pip install flask-login 