from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import (URL, DataRequired, Length, Optional, Regexp,
                                ValidationError)

from .models import URLMap


class URLForm(FlaskForm):
    original_link = URLField(
        'Insert link',
        validators=[DataRequired(message='Required field'),
                    Length(1, 256),
                    URL(require_tld=True, message='Incorrect URL')]
    )
    custom_id = StringField(
        'Type short link',
        validators=[
            Length(1, 16), Optional(),
            Regexp(r'^[A-Za-z0-9]+$',
                   message='Use only [A-Z, a-z, 0-9]')])
    submit = SubmitField('Submit')

    def validate_custom_id(self, field):
        if field.data and URLMap.query.filter_by(short=field.data).first():
            raise ValidationError(f'Имя {field.data} уже занято!')
