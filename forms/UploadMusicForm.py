from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, TextAreaField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed


class UploadMusicForm(FlaskForm):
    name = StringField('Название песни', validators=[DataRequired()])
    img = FileField("Обложка", validators=[])
    tag = SelectField("Тип музыки",  choices=["рок", "реп", "кантри"])
    music = FileField("Музыка", validators=[FileRequired()])
    text_music = TextAreaField("Текст песни", validators=[DataRequired()])
    submit = SubmitField('Загрузить')
