from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class ToDoForm(FlaskForm):
    todo = StringField("To Do", validators=[DataRequired()])
    descriptions = TextAreaField("Description")
    submit = SubmitField("Add To Do")
