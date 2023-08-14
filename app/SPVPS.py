from flask import Flask

#importar views
from views.home_views import home_views
from views.product_view import product_views
from views.report_views import report_views
from views.login_views import login_views
from views.user_views import user_views
from views.sale_views import sale_views
from views.category_views import category_view
from views.brand_views import brand_views
from views.supplier_views import supplier_views

app = Flask(__name__)
app.config['SECRET_KEY'] = 'My secret key'

#registrar views
app.register_blueprint(home_views)
app.register_blueprint(product_views)
app.register_blueprint(report_views)
app.register_blueprint(login_views)
app.register_blueprint(user_views)
app.register_blueprint(sale_views)
app.register_blueprint(category_view)
app.register_blueprint(brand_views)
app.register_blueprint(supplier_views)

if __name__ =='__main__':
    app.run(debug =True)  