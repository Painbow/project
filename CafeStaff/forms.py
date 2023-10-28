from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class StaffSlotForm(FlaskForm):
    shift_type = StringField('Shift Type', validators=[DataRequired()])
    date = StringField('Date', validators=[DataRequired()])
    status = StringField('Status', validators=[DataRequired()])
    submit = SubmitField('Create Slot')