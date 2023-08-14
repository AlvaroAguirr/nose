from flask import Blueprint, render_template, redirect, url_for, flash, abort, request, session
from flask_session import Session
from models.user import User
from forms.login_forms import LoginForm

login_views = Blueprint ('login',__name__)

@login_views.route("/login", methods=('GET', 'POST'))
def login():
    form = LoginForm()

    if form.validate_on_submit():
        nom_usuario = form.nom_usuario.data
        contrasenia = form.contrasenia.data
        user = User.get_by_password(nom_usuario, contrasenia)
        if not user:
            flash('Verifica tus datos')
        else:
            session['user'] = {'nom_usuario': user.nom_usuario, 'rol': user.rol}
            if user.rol == 1:
                return redirect(url_for('login.adm_home'))
            elif user.rol == 2:
                return redirect(url_for('ventas.sale'))
            else:
                flash('Rol inválido', 'error')
    return render_template('login/login.html', form=form)

@login_views.route("/home")
def adm_home():
    return render_template('home/menu_adm.html')

    