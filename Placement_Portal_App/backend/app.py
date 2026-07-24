import sqlite3
from flask import Flask, request, redirect, session
from flask_cors import CORS
from route.admin import AdminRoutes
from route.student import StudentRoutes
from route.company import CompanyRoutes
from apscheduler.schedulers.background import BackgroundScheduler
from config import send_reminders
from config import send_monthly_report
from functools import wraps

admin_routes = AdminRoutes()
student_routes = StudentRoutes()
company_routes = CompanyRoutes()

app = Flask(__name__)
app.secret_key = "cats_and_dogs"
scheduler = BackgroundScheduler()
scheduler.add_job(send_reminders, trigger='cron', hour=22, minute=4)
scheduler.add_job(send_monthly_report, trigger='cron', day=14, hour=22, minute=5)
scheduler.start()
CORS(app, supports_credentials=True,origins=["http://192.168.29.178:8080"])

from functools import wraps
from flask import session

def student_required(f):
    @wraps(f)
    def decorated(id, *args, **kwargs):
        if "student_id" not in session:
            return {"message":"Unauthorized"},401
        if session["student_id"] != id:
            return {"message":"Forbidden"},403
        return f(id,*args,**kwargs)
    return decorated


def admin_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        print(session) 
        if "admin_id" not in session:
            return {"message": "Unauthorized"}, 401
        return f(*args, **kwargs)
    return decorated

def company_required(f):
    @wraps(f)
    def decorated(id, *args, **kwargs):
        print("session company_id:", session["company_id"], type(session["company_id"]))
        print("url id:", id, type(id))
        if "company_id" not in session:
            return {"message":"Unauthorized"},401
        if session["company_id"] != int(id):
            return {"message":"Forbidden"},403
        return f(id,*args,**kwargs)
    return decorated

class Admin:
    @app.route('/a_login', methods=['POST'])
    def admin_login():
        return admin_routes.admin_login()

    @app.route('/admin/a_home')
    @admin_required
    def admin_home():
        return admin_routes.admin_home()

    @app.route('/admin/a_companies', methods=['GET'])
    @admin_required
    def admin_companies():
        return admin_routes.admin_companies()

    @app.route('/admin/a_approval/<approval_status>/<company_id>', methods=['GET'])
    @admin_required
    def admin_u_approval(approval_status, company_id):
        return admin_routes.admin_u_approval(approval_status, company_id)

    @app.route('/admin/a_status/<status>/<company_id>', methods=['GET'])
    @admin_required
    def admin_u_status(status, company_id):
        return admin_routes.admin_u_status(status, company_id)

    @app.route('/admin/a_students', methods=['GET'])
    @admin_required
    def admin_students():
        return admin_routes.admin_students()

    @app.route('/admin/a_s_approval/<approval_status>/<student_id>', methods=['GET'])
    @admin_required
    def admin_s_approval(approval_status, student_id):
        return admin_routes.admin_s_approval(approval_status, student_id)

    @app.route('/admin/a_s_status/<status>/<student_id>', methods=['GET'])
    @admin_required
    def admin_s_status(status, student_id):
        return admin_routes.admin_s_status(status, student_id)

    @app.route('/admin/a_drives', methods=['GET'])
    @admin_required
    def admin_drives():
        return admin_routes.admin_drives()

    @app.route('/admin/a_d_approval/<approval_status>/<drive_id>', methods=['GET'])
    @admin_required
    def admin_d_approval(approval_status, drive_id):
        return admin_routes.admin_d_approval(approval_status, drive_id)

    @app.route('/admin/a_d_status/<status>/<drive_id>', methods=['GET'])
    @admin_required
    def admin_d_status(status, drive_id):
        return admin_routes.admin_d_status(status, drive_id)

class Student:
    @app.route('/s_login', methods=['POST'])
    def student_login():
        return student_routes.student_login()

    @app.route('/s_reg', methods=['POST'])
    def student_signup():
        return student_routes.student_signup()
    
    @app.route('/<id>/s_dash', methods=['GET','POST'])
    @student_required
    def student_dash(id):
        return student_routes.student_dash(id)

    @app.route('/<id>/s_apply', methods=['POST'])
    @student_required
    def student_apply(id):
        return student_routes.student_apply(id)

    @app.route('/<id>/s_appl', methods=['GET'])
    @student_required
    def student_applicationstatus(id):
        return student_routes.student_applicationstatus(id)

    @app.route('/<id>/s_appr', methods=['GET'])
    @student_required
    def student_approved(id):
        return student_routes.student_approved(id)

    @app.route('/<id>/s_profile', methods=['GET'])
    @student_required
    def student_profile(id):
        return student_routes.student_profile(id)

    @app.route('/<id>/s_uprofile', methods=['GET','POST'])
    @student_required
    def student_uprofile(id):
        return student_routes.student_uprofile(id)

    @app.route("/<id>/s_export_csv", methods=["POST"])
    @student_required
    def export_csv(id):
        return student_routes.s_export_csv(id)

    @app.route("/<id>/s_download_csv", methods=["POST"])
    @student_required
    def download_csv(id):
        return student_routes.s_download_csv(id)


class Company:
    @app.route('/c_login', methods=['POST'])
    def company_login():
        return company_routes.company_login()

    @app.route('/c_reg', methods=['POST'])
    def company_register():
        return company_routes.company_signup()

    @app.route('/<id>/c_dash', methods=['GET'])
    @company_required
    def company_dash(id):
        return company_routes.company_dash(id)
    
    @app.route('/<id>/c_cdrive', methods=['GET','POST'])
    @company_required
    def company_cdrive(id):
        return company_routes.company_cdrive(id)

    @app.route('/<id>/c_appl', methods=['GET','POST'])
    @company_required
    def company_applications(id):
        return company_routes.company_appl(id)

    @app.route('/<id>/c_uappl/<x>/<y>', methods=['GET','POST'])
    @company_required
    def company_uapplications(id,x,y):
        return company_routes.company_uappl(id,x,y)

    

@app.route("/logout")
def logout():
    session.clear()
    return {"message":"Logged out"}
        
@app.route('/')
def home():
    return redirect("http://192.168.29.178:8080/")

@app.after_request
def add_header(response):
    response.headers["Cache-Control"]="no-store,no-cache,must-revalidate,max-age=0"
    response.headers["Pragma"]="no-cache"
    response.headers["Expires"]="0"
    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)