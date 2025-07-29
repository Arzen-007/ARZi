from wtforms import TextAreaField
from wtforms.validators import InputRequired

from ARZi.forms import BaseForm
from ARZi.forms.fields import SubmitField


class SendEmailForm(BaseForm):
    text = TextAreaField("Message", validators=[InputRequired()])
    submit = SubmitField("Send")
