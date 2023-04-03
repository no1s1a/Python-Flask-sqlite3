from flask import Flask, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///zamer.db'
db = SQLAlchemy(app)
login_manager = LoginManager(app)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

class Zamer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    NN = db.Column(db.String(50), nullable=False)
    NAME = db.Column(db.String(100), nullable=False)
    mFreeMB = db.Column(db.Float, nullable=False)
    mFreeBX = db.Column(db.Float, nullable=False)
    mFreePL = db.Column(db.Float, nullable=False)
    # ... добавьте остальные столбцы здесь
    dateZ = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    UserZ = db.Column(db.String(80), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('index'))
        else:
            flash('Неверный логин или пароль')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = generate_password_hash(password)
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/')
@login_required
def index():
    zamers = Zamer.query.all()
    return render_template('index.html', zamers=zamers)

# Добавьте маршруты для добавления, удаления и редактирования данных здесь

if __name__ == '__main__':
    app.run(debug=True)
