'''
Created on Jun 15, 2016

@author: ohad
'''
from flask import Flask, render_template, redirect, url_for, flash, request, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.secret_key = 'abcdefg'
db = SQLAlchemy(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or \
                request.form['password'] != 'secret':
            error = 'Invalid credentials'
        else:
            flash('You were successfully logged in')
            return redirect(url_for('index'))
    return render_template('login.html', error=error)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    return 'signup'

@app.route('/creategroup', methods=['GET', 'POST'])
def creategroup():
    return 'create group'

@app.route('/group/<int:id>', methods=['GET', 'POST'])
def group():
    pass

@app.route('/user/<int:user_id>', methods=['GET', 'POST'])
def user():
    return 'user'

@app.route('/pay/<int:id>', methods=['GET', 'POST'])
def pay():
    return 'pay'

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('You were successfully logged out')
    return redirect(url_for('index'))


@app.errorhandler(404)
def file_not_found():
    return 'file not found'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=1)