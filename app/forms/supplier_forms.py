from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, IntegerField
from wtforms.validators import DataRequired, NumberRange

class CreateSupplierForm(FlaskForm):
    nombre = StringField('Nombre', 
                           validators=[DataRequired()])

    localidad = StringField('Localidad', 
                           validators=[DataRequired()])

    telefono = IntegerField('Telefono', 
                           validators=[DataRequired(),  NumberRange(min=0, max=None)])

    direccion = StringField('Direccion', 
                           validators=[DataRequired()])
    
    submit = SubmitField('Guardar')

class UpdateSupplierForm(FlaskForm):
    nombre = StringField('Nombre', 
                           validators=[DataRequired()])

    localidad = StringField('Localidad', 
                           validators=[DataRequired()])

    telefono = IntegerField('Telefono', 
                           validators=[DataRequired(),  NumberRange(min=0, max=None)])

    direccion = StringField('Direccion', 
                           validators=[DataRequired()])
     
    submit = SubmitField('Guardar')