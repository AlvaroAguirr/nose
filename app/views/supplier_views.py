from flask import Blueprint, render_template, redirect ,url_for,request,flash
from models.supplier import Supplier

from forms.supplier_forms import CreateSupplierForm,UpdateSupplierForm
supplier_views = Blueprint ('supplier',__name__)

@supplier_views.route("/supplier/")
def suppliers():
    supplier=Supplier.get_all()
    return render_template('supplier/supplier.html', supplier=supplier )

@supplier_views.route("/supplier/create_sup", methods=('GET','POST'))
def create_sup():
    form=CreateSupplierForm()
    if form.validate_on_submit():
        nombre=form.nombre.data
        localidad= form.localidad.data
        telefono= form.telefono.data
        direccion=form.direccion.data
        sup= Supplier(nombre=nombre,
                      localidad=localidad,
                      telefono=telefono,
                      direccion=direccion)
        sup.save()
        return redirect(url_for('supplier.suppliers'))
    return render_template("/supplier/create_sup.html", form=form)

@supplier_views.route("/supplier/<int:id_proveedor>/editar", methods=('GET','POST'))
def editar_sup(id_proveedor):
    form = UpdateSupplierForm()

    sup = Supplier.get(id_proveedor)

    if form.validate_on_submit():
        sup.nombre=form.nombre.data
        sup.localidad=form.localidad.data
        sup.telefono=form.telefono.data
        sup.direccion=form.direccion.data
        sup.save()
        return redirect(url_for('supplier.suppliers'))
    form.nombre.data=sup.nombre
    form.localidad.data=sup.localidad
    form.telefono.data=sup.telefono
    form.direccion.data=sup.direccion
        
    return render_template("/supplier/create_sup.html", form=form)


@supplier_views.route("/supplier/<int:id_proveedor>/delete", methods=('POST','GET'))
def delete_sup(id_proveedor):
    sup = Supplier.get(id_proveedor)
    sup.delete()
    #enviar datos a form
    return redirect(url_for('supplier.suppliers'))