from flask_wtf import FlaskForm
from wtforms import (
    PasswordField,
    StringField,
    TextAreaField,
    SubmitField,
    BooleanField,
    FileField,
)
from wtforms.validators import DataRequired, Length


class EditNews(FlaskForm):
    title = StringField(
        "Заголовок",
        validators=[DataRequired(), Length(max=100)],
    )
    picture = FileField(
        "Изображение",
    )
    text = TextAreaField(
        "Текст новости",
        validators=[DataRequired(), Length(max=500)],
    )
    is_published = BooleanField("Опубликовано")
    submit = SubmitField("Сохранить")
