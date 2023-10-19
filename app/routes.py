from app import app
from flask import render_template
from datetime import datetime


@app.route('/')
@app.route('/index')
def index():
    admin = {'username': 'Aboudi'}
    users = {'Mike', 'Moe'}

    return render_template('index.html', admin=admin, datetime=datetime.now(), users=users)
