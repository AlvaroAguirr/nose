from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, SubmitField, SelectField, DateField, IntegerField, FloatField
from wtforms.validators import DataRequired, NumberRange

class CreateSaleForm(FlaskForm):

    pros=[]
    uses=[]

    fecha = DateField('Fecha', 
                           validators=[DataRequired()])
    
    unidades_vendidas = IntegerField('Unidades Vendidas', validators=[DataRequired(),  NumberRange(min=0, max=None)])

    id_producto = SelectField('Producto', choices=pros, coerce=int, validate_choice=False, validators=[DataRequired()])

    id_usuario = SelectField('Usuario', choices=uses, coerce=int, validate_choice=False, validators=[DataRequired()])
    

    total = DecimalField('Total', validators=[DataRequired(), NumberRange(min=0.0, max=None)])
    
    submit = SubmitField('Guardar')