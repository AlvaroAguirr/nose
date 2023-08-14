from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class CreateBrandForm(FlaskForm):
    nombre = StringField('Nombre', 
                           validators=[DataRequired()])
    
    submit = SubmitField('Guardar')

class UpdateBrandForm(FlaskForm):
    nombre = StringField('nombre', 
                           validators=[DataRequired()])
     
    submit = SubmitField('Guardar')