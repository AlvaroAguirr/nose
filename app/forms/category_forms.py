from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class CreateCategoryForm(FlaskForm):
    nombre = StringField('Categoria', 
                           validators=[DataRequired()])

    submit = SubmitField('Guardar')

class UpdateCategoryForm(FlaskForm):
    nombre = StringField('Categoria', 
                           validators=[DataRequired()])

    submit = SubmitField('Actualizar')