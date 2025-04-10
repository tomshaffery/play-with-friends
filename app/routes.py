from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import SearchForm

@app.route('/')
@app.route('/index')
def index():
   return render_template('index.html', title='Play With Friends')

@app.route('/search', methods=['GET', 'POST'])
def search():
   form = SearchForm()
   if form.validate_on_submit():
      flash('Search commencing.')
      return redirect(url_for('results'))
   return render_template('search.html', title='Find New Games', form=form)

@app.route('/results')
def results():
   return render_template('results.html', title='New Games To Play')