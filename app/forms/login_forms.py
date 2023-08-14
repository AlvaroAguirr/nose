from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField, EmailField, 
                     SubmitField, ValidationError)
from wtforms.validators import DataRequired, Email, EqualTo, Length
from flask_wtf.file import FileField, FileRequired, FileAllowed

from models.user import User

        
################# Formulario de Login ##################
class LoginForm(FlaskForm):
    nom_usuario = StringField('Nom_Usuario', validators=[DataRequired()])
    contrasenia = PasswordField('Contrasenia', validators=[DataRequired()])
    submit = SubmitField('Ingresar')
