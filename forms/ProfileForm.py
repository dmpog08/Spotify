from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, DateField
from wtforms.validators import DataRequired
from wtforms.fields import EmailField
from flask_wtf.file import FileField, FileRequired, FileAllowed


class ProfileForm(FlaskForm):
    name = StringField('Имя', validators=[DataRequired()])
    sename = StringField('Фамилия', validators=[DataRequired()])
    nickname = StringField('Никнейм', validators=[DataRequired()])
    phone = IntegerField('телефон', validators=[DataRequired()])
    email = EmailField('Почта', validators=[DataRequired()])
    img = FileField("Аватарка", validators=[])
    birthday = DateField('День рождения', format='%Y-%m-%d')
    submit = SubmitField('Загрузить')