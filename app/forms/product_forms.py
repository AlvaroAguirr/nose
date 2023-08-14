from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField,TextAreaField, SelectField, DecimalField
from wtforms.validators import DataRequired, NumberRange
from flask_wtf.file import FileField, FileAllowed

class CreateProductForm(FlaskForm):

    cats=[]
    marc=[]

    nombre = StringField('Nombre', 
                           validators=[DataRequired()])

    precio = DecimalField('Precio', 
                           validators=[DataRequired(), NumberRange(min=0.0, max=None)])

    descripcion = StringField('Descripcion', 
                           validators=[DataRequired()])

    id_marca = SelectField('Marca',
                           choices=marc, coerce=int, validate_choice=False, validators=[DataRequired()])
    
    id_categoria = SelectField('Categoria', 
                           choices=cats, coerce=int, validate_choice=False, validators=[DataRequired()])
    
    Unidades = IntegerField('Unidades',
                            validators=[DataRequired(), NumberRange(min=0.0, max=None)])
    
    submit = SubmitField('Guardar')
 
class UpdateProductForm(FlaskForm):

    cats=[]
    marc=[]

    nombre = StringField('Nombre', 
                           validators=[DataRequired()])

    precio = DecimalField('precio', 
                           validators=[DataRequired(), NumberRange(min=0.0, max=None)])

    descripcion = StringField('descripcion', 
                           validators=[DataRequired()])

    id_marca = SelectField('marca',
                           choices=marc, coerce=int, validate_choice=False, validators=[DataRequired()])
    
    id_categoria = SelectField('categoria', 
                           choices=cats, coerce=int, validate_choice=False, validators=[DataRequired()])
    
    Unidades = IntegerField('Unidades',
                            validators=[DataRequired(), NumberRange(min=0.0, max=None)])
    
    submit = SubmitField('Actualizar')