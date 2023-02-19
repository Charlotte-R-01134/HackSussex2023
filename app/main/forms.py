from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Regexp


class NewNoteForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(1, 64)])
    submit = SubmitField('Create Note')

class NoteForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(1, 64)])
    content = StringField('Content', validators=[DataRequired(), Length(1, 10000)])
    submit = SubmitField('Edit Note')