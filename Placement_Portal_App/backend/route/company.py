import sqlite3
from flask import Flask, jsonify, request, redirect, Response,session
from datetime import date

class CompanyRoutes:

    def company_signup(self):
        conn = sqlite3.connect('Placement_Portal.db')
        cursor = conn.cursor()
        req = request.form
        l = []
        for k, v in req.items():
            l.append(v)
        cursor.execute('''INSERT INTO COMPANY(NAME, HR_CONTACT, WEBSITE, PASSWORD) VALUES(?,?,?,?)''', l)
        conn.commit()
        conn.close()
        return redirect("http://192.168.29.178:8080/login")

    def company_login(self, methods=['GET','POST']):
        conn = sqlite3.connect('Placement_Portal.db')
        cursor = conn.cursor()
        req = request.form
        l = []
        for k, v in req.items():
            l.append(v)
        cursor.execute('''SELECT NAME FROM COMPANY''')
        comp = cursor.fetchall()
        t = (l[0],)
        if t in comp:
            cursor.execute('''SELECT ID FROM COMPANY WHERE NAME = ?''',(l[0],))
            id = cursor.fetchone()
            cursor.execute('''SELECT PASSWORD FROM COMPANY WHERE ID = ?''', (id))
            password = cursor.fetchone()
            if password[0] == l[1]:
                cursor.execute('''SELECT APPROVAL_STATUS FROM COMPANY WHERE ID = ?''', (id))
                a_status = cursor.fetchone()
                if a_status[0] == "APPROVED":
                    cursor.execute('''SELECT STATUS FROM COMPANY WHERE ID = ?''', (id))
                    status = cursor.fetchone()
                    conn.close()
                    if status[0] != "BLACKLISTED":
                        session["company_id"] = id[0]
                        return redirect("http://192.168.29.178:8080/" + str(id[0]) + "/c_dash")
                    else:
                        return Response('<script>alert("Company Blacklisted"); window.history.back();</script>',mimetype="text/html")
                elif a_status[0] == "PENDING":
                    return Response('<script>alert("Company not Approved"); window.history.back();</script>',mimetype="text/html")
                else:
                    return Response('<script>alert("Company account creation rejected"); window.history.back();</script>',mimetype="text/html")
            else:
                return Response('<script>alert("Incorrect password"); window.history.back();</script>',mimetype="text/html")
        else:
            conn.close()
            return Response('<script>alert("Company not found"); window.history.back();</script>',mimetype="text/html")

    def company_dash(self, id, methods=['POST']):
        conn = sqlite3.connect('Placement_Portal.db')
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM COMPANY WHERE ID = ?''',(id,))
        comp = cursor.fetchall()
        cursor.execute(
            '''SELECT * FROM DRIVE WHERE COMPANY_ID = ?''',(id,)
        )
        drive = cursor.fetchall()
        c = []
        for i in range(0, len(drive)):
            cursor.execute('''SELECT D.TITLE, COUNT(A.ID) FROM APPLICATION AS A LEFT JOIN DRIVE AS D ON A.DRIVE_ID = D.ID WHERE A.DRIVE_ID = ?''',(drive[i][0],))
            count = cursor.fetchall()
            c.append(count)
        return jsonify({
            "comp" : comp,
            "drive" : drive,
            "c" : c
        })

    def company_cdrive(self, id, methods=['GET','POST']):
        conn = sqlite3.connect('Placement_Portal.db')
        cursor = conn.cursor()
        req = request.form
        l = []
        for k, v in req.items():
            l.append(v)
        cursor.execute('''INSERT INTO DRIVE(COMPANY_ID, TITLE, DESCRIPTION, ELIGIBILITY_CRITERIA, APPLICATION_DEADLINE, VACANCIES, PLACED) VALUES(?,?,?,?,?,?,?)''',(id,l[0],l[1],l[2],l[3],l[4],l[5],))
        conn.commit()
        conn.close()
        return redirect("http://192.168.29.178:8080/" + id + "/c_cdrive")

    def company_appl(self, id, methods=['GET','POST']):
        conn = sqlite3.connect('Placement_Portal.db')
        cursor = conn.cursor()
        cursor.execute('''SELECT A.ID, A.STUDENT_ID, A.DRIVE_ID, A.APPLICATION_DATE, A.STATUS FROM APPLICATION AS A RIGHT JOIN DRIVE AS D ON A.DRIVE_ID = D.ID WHERE D.COMPANY_ID = ?''',(id,))
        applications = cursor.fetchall()
        return jsonify(applications)

    def company_uappl(self, id, x, y):
        conn = sqlite3.connect('Placement_Portal.db')
        cursor = conn.cursor()
        cursor.execute('''UPDATE APPLICATION SET STATUS = ? WHERE ID = ?''', (x, y))
        conn.commit()
        conn.close()
        return redirect("http://192.168.29.178:8080/" + id + "/c_appl")