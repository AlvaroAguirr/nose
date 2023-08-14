from flask import Blueprint, render_template, redirect ,url_for,request,flash
from models.brand import Brand
import math

from forms.brand_forms import CreateBrandForm, UpdateBrandForm
brand_views = Blueprint ('brand',__name__)

@brand_views.route("/Marca/")
@brand_views.route("/Marca/<int:page>")
def brands(page=1):
    limit =10
    brand=Brand.get_all(limit = limit,page=page)
    total_br=Brand.count()
    pages= math.ceil(total_br / limit)
    return render_template('brand/brand.html',brand=brand, page=page, pages=pages)

@brand_views.route("/Marca/crear", methods=('GET','POST'))
def create_bra():
    form= CreateBrandForm()
    if form.validate_on_submit():
        nombre= form.nombre.data
        br = Brand(nombre)
        br.save()
        return redirect(url_for('brand.brands'))
    return render_template("/brand/create_bra.html", form=form )

@brand_views.route("/Marca/<int:id_marca>/Editar", methods=('GET','POST'))
def editar_bra(id_marca):
    form = UpdateBrandForm()
    bra = Brand.get(id_marca)
    if form.validate_on_submit():
        bra.nombre=form.nombre.data
        bra.save()
        return redirect(url_for('brand.brands'))
    form.nombre.data =bra.nombre
    return render_template('/brand/editar_bra.html', form=form)

@brand_views.route("/Marca/<int:id_marca>/Editar", methods=('POST',))
def eliminar_bra(id_marca):
    br =Brand.get(id_marca)
    br.delete()
    return render_template('/brand/create_bra.html')
