from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from pyodbc import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://Onlinestore:Gst989998@FindBite'
app.debug=True
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(110), unique=True)
    password = db.Column(db.String(40))

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
    
    def __repr__(self):
        return '<User %r>' % self.username

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/logedin')
def logedin():
    return render_template('logedin.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/post_user', methods=['GET', 'POST'])
def post_user():
        user = User(request.form['username'], request.form['email'],request.form['password'])
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('index'))

if __name__ == "__main__":
    app.run()