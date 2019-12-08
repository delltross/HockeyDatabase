from flask import render_template

from app import app
from display import get_players()

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', players=get_players())