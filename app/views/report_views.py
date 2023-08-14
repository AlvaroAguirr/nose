from flask import Blueprint, render_template
from models.reports import Reports

report_views = Blueprint('report',__name__)

@report_views .route("/reportes/")
def reports ():
    reports = Reports.get_all()
    return render_template('reports/reports.html',
                           reports= reports)