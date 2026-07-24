import sqlite3
from flask import Flask, jsonify, request, redirect, Response, send_file, session
from datetime import date
import os, csv, threading, requests
from config import WEBHOOK

class StudentRoutes:
    def student_signup(self):
        conn = sqlite3.connect('Placement_Portal.db')
        cursor = conn.cursor()
        req = request.form
        l = []
        for k, v in req.items():
            l.append(v)
        cursor.execute('''SELECT ID FROM STUDENT''')
        ids = cursor.fetchall()
        if (l[0],) in ids:
            return Response('<script>alert("ID already exists"); window.history.back();</script>',mimetype="text/html")
        else:
            cursor.execute('''INSERT INTO STUDENT(ID, NAME, BRANCH, CONTACT_NUMBER, CGPA, YEAR, PASSWORD) VALUES(?,?,?,?,?,?,?)''', l)
        conn.commit()
        conn.close()
        return redirect("http://192.168.29.178:8080/login")
        
    def student_login(self,methods=['POST']):
        conn = sqlite3.connect('Placement_Portal.db')
        cursor = conn.cursor()
        req = request.form
        l = []
        for k, v in req.items():
            l.append(v)
        cursor.execute('''SELECT ID FROM STUDENT''')
        users = cursor.fetchall()
        if (l[0],) in users:
            cursor.execute('''SELECT PASSWORD FROM STUDENT WHERE ID = ?''', (l[0],))
            password = cursor.fetchone()
            if password[0] == l[1]:
                cursor.execute('''SELECT APPROVAL_STATUS FROM STUDENT WHERE ID = ?''', (l[0],))
                a_status = cursor.fetchone()
                if a_status[0] == "APPROVED":
                    cursor.execute('''SELECT STATUS FROM STUDENT WHERE ID = ?''', (l[0],))
                    status = cursor.fetchone()
                    conn.close()
                    if status[0] != "BLACKLISTED":
                        session["student_id"] = l[0]
                        return redirect("http://192.168.29.178:8080/" + l[0] + "/s_dash")
                    else:
                        return Response('<script>alert("User Blacklisted"); window.history.back();</script>',mimetype="text/html")
                elif a_status[0] == "PENDING":
                    return Response('<script>alert("User not Approved"); window.history.back();</script>',mimetype="text/html")
                else:
                    return Response('<script>alert("User account creation rejected"); window.history.back();</script>',mimetype="text/html")
            else:
                return Response('<script>alert("Incorrect password"); window.history.back();</script>',mimetype="text/html")
        else:
            conn.close()
            return Response('<script>alert("User not found"); window.history.back();</script>',mimetype="text/html")
    
    def student_dash(self, id, methods=['GET','POST']):
        conn = sqlite3.connect('Placement_Portal.db')
        cursor = conn.cursor()
        cursor.execute('''SELECT D.ID, C.NAME, D.TITLE, D.DESCRIPTION, D.ELIGIBILITY_CRITERIA, D.APPLICATION_DEADLINE, D.APPROVAL_STATUS, D.STATUS, A.STUDENT_ID, A.DRIVE_ID FROM DRIVE AS D 
                       JOIN COMPANY AS C ON D.COMPANY_ID = C.ID LEFT JOIN APPLICATION AS A ON D.ID = A.DRIVE_ID AND A.STUDENT_ID = ? WHERE D.APPROVAL_STATUS="APPROVED" AND D.STATUS!="REVOKED" 
                       AND A.DRIVE_ID IS NULL''',(id,))
        drives = cursor.fetchall()
        eligible_drives = []
        cursor.execute("SELECT CGPA, YEAR FROM STUDENT WHERE ID = ?",(id,))
        student = cursor.fetchone()
        student_cgpa = float(student[0])
        student_year = str(student[1])
        for drive in drives:
            cgpa_req, year_req = drive[4].split("-")
            if student_cgpa >= float(cgpa_req) and student_year == year_req:
                eligible_drives.append(drive)
        conn.close()
        return jsonify(eligible_drives)
    
    def student_apply(self, id, methods=['POST']):
        conn = sqlite3.connect('Placement_Portal.db')
        cursor = conn.cursor()
        req = request.form
        l = []
        for i, j in req.items():
            l.append(j)
        application_date = date.today()
        cursor.execute('''INSERT INTO APPLICATION(STUDENT_ID, DRIVE_ID, APPLICATION_DATE) VALUES(?,?,?)''',(id,l[0],application_date,))
        conn.commit()
        conn.close()
        return redirect("http://192.168.29.178:8080/" + id + "/s_dash")

    def student_applicationstatus(self, id, methods=['GET']):
        conn = sqlite3.connect('Placement_Portal.db')
        cursor = conn.cursor()
        cursor.execute('''SELECT A.ID, D.TITLE, D.DESCRIPTION, A.APPLICATION_DATE, A.STATUS, C.NAME FROM APPLICATION AS A LEFT JOIN DRIVE AS D ON A.DRIVE_ID = D.ID 
        LEFT JOIN COMPANY AS C ON D.COMPANY_ID = C.ID WHERE A.STUDENT_ID = ? AND A.STATUS != "APPROVED"''',(id,))
        appl = cursor.fetchall()
        conn.close()
        return jsonify(appl)

    def student_approved(self, id, methods=['GET']):
        conn = sqlite3.connect('Placement_Portal.db')
        cursor = conn.cursor()
        cursor.execute('''SELECT A.ID, D.TITLE, D.DESCRIPTION, A.APPLICATION_DATE, A.STATUS, C.NAME FROM APPLICATION AS A LEFT JOIN DRIVE AS D ON A.DRIVE_ID = D.ID 
                LEFT JOIN COMPANY AS C ON D.COMPANY_ID = C.ID WHERE A.STUDENT_ID = ? AND A.STATUS = "APPROVED"''',(id,))
        appr = cursor.fetchall()
        conn.close()
        return jsonify(appr)

    def student_profile(self, id, methods=['GET','POST']):
        conn = sqlite3.connect('Placement_Portal.db')
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM STUDENT WHERE ID = ?''',(id,))
        profile = cursor.fetchall()
        conn.close()
        return jsonify(profile[0])

    def student_uprofile(self,id):
        conn = sqlite3.connect('Placement_Portal.db')
        cursor = conn.cursor()
        res = request.form
        l = []
        for k, v in res.items():
            l.append(v)
        cursor.execute('''UPDATE STUDENT SET NAME=?, BRANCH=?, CONTACT_NUMBER=?, CGPA=?, YEAR=?, PASSWORD=? WHERE ID = ?''',(l[0],l[1],l[2],l[3],l[4],l[5],id,))
        conn.commit()
        conn.close()
        return redirect("http://192.168.29.178:8080/" + id + "/s_dash")
        
    def create_csv(self, id, methods=['GET','POST']):
        conn = sqlite3.connect("Placement_Portal.db")
        cursor = conn.cursor()
        cursor.execute("""SELECT A.STUDENT_ID, C.NAME, D.TITLE, A.STATUS, A.APPLICATION_DATE FROM APPLICATION A JOIN DRIVE D ON A.DRIVE_ID = D.ID JOIN COMPANY C ON D.COMPANY_ID = C.ID WHERE A.STUDENT_ID = ?""",(id,))
        data = cursor.fetchall()
        conn.close()
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        EXPORT_DIR = os.path.join(BASE_DIR, "exports")
        os.makedirs(EXPORT_DIR, exist_ok=True)
        filename = os.path.join(EXPORT_DIR, f"student_{id}.csv")
        with open(filename,"w",newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Student ID", "Company", "Drive", "Status", "Application Date"])
            writer.writerows(data)

    def s_export_csv(self, id):
        thread = threading.Thread(target=self.create_csv, args=(id,))
        thread.start()
        return Response('<script>alert("Export Started"); window.history.back();</script>',mimetype="text/html")

    def s_download_csv(self, id, methods=['GET','POST']):
        requests.post(WEBHOOK,json={"text": f"✅ CSV Export Completed for Student {id}"})
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        EXPORT_DIR = os.path.join(BASE_DIR, "exports")
        filename = os.path.join(EXPORT_DIR, f"student_{id}.csv")
        return send_file(filename, as_attachment=True)