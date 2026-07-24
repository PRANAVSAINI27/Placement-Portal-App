import sqlite3
from flask import Flask, request, redirect, jsonify, Response, session

class AdminRoutes:
    def admin_login(self, method=['POST']):
        conn = sqlite3.connect('Placement_Portal.db')
        cursor = conn.cursor()
        req = request.form
        l = []
        for k, v in req.items():
            l.append(v)
        cursor.execute('''SELECT ID FROM ADMIN''')
        users = cursor.fetchall()
        if (l[0],) in users:
            cursor.execute('''SELECT PASSWORD FROM ADMIN WHERE ID = ?''', (l[0],))
            password = cursor.fetchone()
            conn.close()
            if password[0] == l[1]:
                session["admin_id"] = l[0]
                return redirect("http://192.168.29.178:8080/admin/a_home")
            else:
                return Response(
            '<script>alert("Incorrect password"); window.history.back();</script>',mimetype="text/html")

        else:
            conn.close()
            return Response(
        '<script>alert("User not found"); window.history.back();</script>',mimetype="text/html")
    
    def admin_companies(self):
        conn = sqlite3.connect('Placement_Portal.db')
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM COMPANY''')
        companies = cursor.fetchall()
        conn.close()
        return jsonify(companies)

    def admin_u_approval(self, approval_status='PENDING', company_id=None, method='GET'):
        conn = sqlite3.connect('Placement_Portal.db')
        cursor = conn.cursor()
        cursor.execute('''UPDATE COMPANY SET APPROVAL_STATUS = ? WHERE ID = ?''', (approval_status, company_id))
        conn.commit()
        conn.close()
        return redirect("http://192.168.29.178:8080/admin/a_companies")
    
    def admin_u_status(self, status='ACTIVE', company_id=None, method='POST'):
        conn = sqlite3.connect('Placement_Portal.db')
        cursor = conn.cursor()
        cursor.execute('''UPDATE COMPANY SET STATUS = ? WHERE ID = ?''', (status, company_id))
        if status != 'ACTIVATED':
            cursor.execute('''UPDATE DRIVE SET STATUS = 'REVOKED' WHERE COMPANY_ID = ?''', (company_id,))
        conn.commit()
        conn.close()
        return redirect("http://192.168.29.178:8080/admin/a_companies")
    
    def admin_students(self):
        conn = sqlite3.connect('Placement_Portal.db')
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM STUDENT''')
        students = cursor.fetchall()
        conn.close()
        return jsonify(students)
    
    def admin_s_approval(self, approval_status='PENDING', student_id=None, method='GET'):
        conn = sqlite3.connect('Placement_Portal.db')
        cursor = conn.cursor()
        cursor.execute('''UPDATE STUDENT SET APPROVAL_STATUS = ? WHERE ID = ?''', (approval_status, student_id))
        conn.commit()
        conn.close()
        return redirect("http://192.168.29.178:8080/admin/a_students")
    
    def admin_s_status(self, status='ACTIVE', student_id=None, method='GET'):
        conn = sqlite3.connect('Placement_Portal.db')
        cursor = conn.cursor()
        cursor.execute('''UPDATE STUDENT SET STATUS = ? WHERE ID = ?''', (status, student_id))
        conn.commit()
        conn.close()
        return redirect("http://192.168.29.178:8080/admin/a_students")
    
    def admin_drives(self):
        conn = sqlite3.connect('Placement_Portal.db')
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM DRIVE''')
        drives = cursor.fetchall()
        conn.close()
        return jsonify(drives)
    
    def admin_d_approval(self, approval_status='PENDING', drive_id=None, method='GET'):
        conn = sqlite3.connect('Placement_Portal.db')
        cursor = conn.cursor()
        cursor.execute('''UPDATE DRIVE SET APPROVAL_STATUS = ? WHERE ID = ?''', (approval_status, drive_id))
        conn.commit()
        conn.close()
        return redirect("http://192.168.29.178:8080/admin/a_drives")
    
    def admin_d_status(self, status='ACTIVE', drive_id=None, method='GET'):
        conn = sqlite3.connect('Placement_Portal.db')
        cursor = conn.cursor()
        cursor.execute('''UPDATE DRIVE SET STATUS = ? WHERE ID = ?''', (status, drive_id))
        conn.commit()
        conn.close()
        return redirect("http://192.168.29.178:8080/admin/a_drives")

    def admin_home(self):
        conn = sqlite3.connect('Placement_Portal.db')
        cursor = conn.cursor()
        cursor.execute('''SELECT COUNT(*) FROM COMPANY WHERE APPROVAL_STATUS = 'APPROVED' AND STATUS = 'ACTIVATED' ''')
        company_count = cursor.fetchone()[0]
        cursor.execute('''SELECT COUNT(*) FROM STUDENT WHERE APPROVAL_STATUS = 'APPROVED' AND STATUS = 'ACTIVATED' ''')
        student_count = cursor.fetchone()[0]
        cursor.execute('''SELECT COUNT(*) FROM DRIVE WHERE APPROVAL_STATUS = 'APPROVED' AND STATUS = 'ACTIVATED' ''')
        drive_count = cursor.fetchone()[0]
        conn.close()
        return jsonify({
            "companies": company_count,
            "students": student_count,
            "drives": drive_count,
        })
        
