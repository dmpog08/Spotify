from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms import BooleanField, SubmitField
from wtforms.validators import DataRequired


class Comment(FlaskForm):
    content = TextAreaField("Комментарий")
    submit = SubmitField('Отправить')