from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Flask'}
    posts = [
        {
            'author': {'username': 'Django'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Java'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)