from flask_wtf import FlaskForm
from flask_table import Table, Col, LinkCol
from wtforms import FieldList, FormField, StringField, PasswordField, BooleanField, SubmitField, DateField, IntegerField
from wtforms.validators import DataRequired, Optional


''' some elements for tables'''

class CompositionResults(Table):
    id_music = Col('Music ID')
    composer = Col('Composer')
    title = Col("Composition Title")
    opus_num = Col("Opus Number")
    date = Col("Composition Date")
    notation_filename = Col("Notation filename")
    instrumentation = Col("Instrumentation")
    edit = LinkCol('Edit', 'edit', url_kwargs=dict(id='id_music'))

''' Full page forms'''
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class SodbMusicForm(FlaskForm):
    id_music = IntegerField('Music ID', validators=[Optional()])
    composer = StringField('Composer (Last, First)', validators=[DataRequired()])
    title = StringField("Composition Title", validators=[DataRequired()])
    opus_num = IntegerField("Opus Number", validators=[DataRequired()])
    date = DateField("Composition Date", validators=[Optional()])
    notation_filename = StringField("Notation filename", validators=[DataRequired()])
    instrumentation = StringField("Instrumentation", validators=[Optional()])
    submit = SubmitField('Add Entry')
    search = SubmitField('Search')

class SodbListCompositionsForm(FlaskForm):
    id_music = IntegerField('Music ID', validators=[Optional()])
    composer = StringField('Composer (Last, First)', validators=[Optional()])
    title = StringField("Composition Title", validators=[Optional()])
    opus_num = IntegerField("Opus Number", validators=[Optional()])
    date = DateField("Composition Date", validators=[Optional()])
    notation_filename = StringField("Notation filename", validators=[Optional()])
    instrumentation = StringField("Instrumentation", validators=[Optional()])
    search = SubmitField('Search')

