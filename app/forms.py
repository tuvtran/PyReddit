from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import Required, URL


class PostForm(FlaskForm):
    title = StringField('Title', [Required()])
    text = TextAreaField('Body text')
    link = StringField('Link', [URL(
        require_tld=True, message='That is a not a valid URL!')])
