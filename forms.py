from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired


class JobForm(FlaskForm):
    company = StringField('Company')
    role = StringField('Role')
    status = SelectField('Status', choices=[
        ('Applied', 'Applied'),
        ('Interview', 'Interview'),
        ('Offer', 'Offer'),
        ('Rejected', 'Rejected')
    ])
    submit = SubmitField('Add Job')
