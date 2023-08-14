from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, IntegerField
from wtforms.validators import DataRequired, NumberRange

class CreateUserForm(FlaskForm):
    nombre = StringField('Nombre', 
                           validators=[DataRequired()])

    ape_paterno = StringField('Apellido paterno', 
                           validators=[DataRequired()])

    ape_materno = StringField('Apellido materno', 
                           validators=[DataRequired()])

    nom_usuario = StringField('Nombre de usuario', 
                           validators=[DataRequired()])
    
    contrasenia = StringField('Contraseña', 
                           validators=[DataRequired()])
    rol =  IntegerField('Rol', validators=[DataRequired(),  NumberRange(min=1, max=2)])
    
    submit = SubmitField('Guardar')

class UpdateUserForm(FlaskForm):
    nombre = StringField('nombre', 
                           validators=[DataRequired()])

    ape_paterno = StringField('Apellido paterno', 
                           validators=[DataRequired()])

    ape_materno = StringField('Apellido materno', 
                           validators=[DataRequired()])

    nom_usuario = StringField('Nombre de usuario', 
                           validators=[DataRequired()])
    
    contrasenia = StringField('Contraseña', 
                           validators=[DataRequired()])
    
    rol =  IntegerField('Rol', validators=[DataRequired(),  NumberRange(min=1, max=2)])
     
    submit = SubmitField('Guardar')