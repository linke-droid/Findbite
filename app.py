from flask import Flask, render_template, request, redirect, url_for
import requests
from flask_sqlalchemy import SQLAlchemy
from pyodbc import *
import json
import requests
import api
from config import sqlstring

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = sqlstring()
app.debug = True
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


db.create_all()
db.session.add(
    User(username='admin', email='admin@example.com', password='123'))


@app.route('/result', methods=['GET'])
def result():
    req = requests.get(
        'https://maps.googleapis.com/maps/api/place/textsearch/json?query=restaurants+toronto+canada&key=AIzaSyDBzaptmbm9nuWuFAbjsyxEsz5OGbB0oIs')
    data = json.loads(req.content)
    return render_template('result.html', data=data)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api-test', methods=['POST'])
def demo():
    protein_food = request.form['Proteinkälla']
    type_food = request.form['Typ_av_mat']
    print(type_food)
    price_food = request.form['price']
    result = api.get_restaurants(protein_food, type_food, price_food)
    print(result)

    print("HÄR ÄR DET VI VILL SEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")

    return render_template('demo.html', restaurants=result)


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


@app.route('/myinfo')
def myinfo():
    return render_template('myinfo.html')


@app.route('/editmyinfo')
def edit_myinfo():
    return render_template('edit_myinfo.html')


@app.route('/post_user', methods=['POST'])
def post_user():
    user = User(request.form['username'],
                request.form['email'], request.form['password'])
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/check_login', methods=['GET', 'POST'])
def log_in():
    if request.method == "POST":
        user_name = request.form['username']
        pass_word = request.form['password']
        res = User.query.filter_by(
            username=user_name, password=pass_word).all()
        if not res:
            return render_template('wronglogin.html')
        else:
            return render_template('logedin.html')
    else:
        return render_template('index.html')


@app.route('/push_new_info', methods=['GET', 'POST'])
def push_new_info(id):
    found_user = User.query.get(id)
    if request.method == "POST":
        found_user.username = request.form['username']
        found_user.password = request.form['password']
        found_user.email = request.form['email']
        db.session.add(found_user)
        db.session.commit()
        return redirect(url_for('index'))
    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run()
