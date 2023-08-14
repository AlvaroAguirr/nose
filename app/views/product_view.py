import math
from flask import Blueprint, render_template, redirect, url_for,request, flash
from models.product import Product

from forms.product_forms import CreateProductForm,UpdateProductForm

from models. categories import Category
from models.brand import Brand

product_views =Blueprint ('product',__name__)

@product_views.route("/productos")
@product_views.route("/productos/<int:page>/")
def productos(page=1):
    product = Product.get_all2()
    limit =10
    product = Product.get_all2(limit=limit, page=page)
    total_products= Product.count()
    pages = math.ceil(total_products / limit)
    return render_template('/product/product.html',
                           product=product, pages=pages, page=page)

@product_views.route("/crear_productos", methods=('GET','POST'))
def c_produ():
    form= CreateProductForm()
    categories = Category.get_all()
    cats=[(-1, '')]
    for cat in categories:
        cats.append((cat.id_categoria, cat.nombre))
    form.id_categoria.choices = cats

    brands = Brand.get_all()
    marc=[(-1, 'selecciona')]
    for brand in brands:
        marc.append((brand.id_marca, brand.nombre))
    form.id_marca.choices = marc

    if form.validate_on_submit():
        nombre= form.nombre.data
        precio=form.precio.data
        descripcion=form.descripcion.data
        unidades=form.Unidades.data
        id_marca=form.id_marca.data
        id_categoria= form.id_categoria.data
        prod= Product(nombre=nombre,
                      precio=precio,
                      descripcion=descripcion,
                      Unidades=unidades,
                      id_categoria=id_categoria,
                      id_marca=id_marca)

        prod.save()
        return redirect(url_for('product.productos'))
    return render_template('product/create_pro.html', form=form)



@product_views.route("/productos/<int:id_producto>/actualizar", methods=('GET','POST'))
def updateprod(id_producto):
    form=UpdateProductForm()

    categories = Category.get_all()
    cats=[(-1, '')]
    for cat in categories:
        cats.append((cat.id_categoria, cat.nombre))
    form.id_categoria.choices = cats

    brands = Brand.get_all()
    marc=[(-1, 'selecciona')]
    for brand in brands:
        marc.append((brand.id_marca, brand.nombre))
    form.id_marca.choices = marc

    prod=Product.get(id_producto)
    
    if form.validate_on_submit():
        prod.nombre=form.nombre.data
        prod.precio=form.precio.data
        prod.descripcion=form.descripcion.data
        prod.Unidades=form.Unidades.data
        prod.id_marca=form.id_marca.data
        prod.id_categoria=form.id_categoria.data
        prod.save()
        return redirect(url_for('product.productos'))
    form.nombre.data=prod.nombre
    form.precio.data=prod.precio
    form.descripcion.data=prod.descripcion
    form.Unidades.data=prod.Unidades
    form.id_marca.data=prod.id_marca
    form.id_categoria.data= prod.id_categoria
    return render_template('/product/update_prod.html',form=form)

@product_views.route("/productos/<int:id_producto>/eliminar", methods=('POST',))
def delprod(id_producto):

    prod= Product.get(id_producto)
    prod.delete()
    page = request.form['page']
    return redirect(url_for('product.productos', page=page))