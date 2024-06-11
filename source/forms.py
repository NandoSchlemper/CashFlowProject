from models import User, roles
from flask_wtf import FlaskForm
import wtforms as w

class UserForm(FlaskForm):
    name = w.StringField('Name', validators=[w.validators.DataRequired(), w.validators.Length(max=55)])
    email = w.StringField('Email', validators=[w.validators.DataRequired(), w.validators.Length(max=55), w.validators.Email()])
    password = w.StringField('Password', validators=[w.validators.DataRequired(), w.validators.Length(max=50)])
    role = w.FieldList('Role', choices=[
        (roles.ADM, 'Administrator'),
        (roles.FIN, 'Financial'),
        (roles.OPE, 'Operational')
        (roles.HR, 'Human Resources'),
        (roles.ALM, 'Warehouse')
    ], validators=[w.validators.DataRequired()])

    submit = w.SubmitField('Submit')

