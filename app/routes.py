from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import SearchForm

@app.route('/')
@app.route('/index')
def index():
   return render_template('index.html', title='Play With Friends')

@app.route('/search')
def search():
   form = SearchForm()
   return render_template('search.html', title='Find New Games', form=form)