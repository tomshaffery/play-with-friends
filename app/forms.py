from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class SearchForm(FlaskForm):
    user = StringField('You', validators=[DataRequired()])
    friend = StringField('Friend', validators=[DataRequired()])
    submit = SubmitField('Find Games')