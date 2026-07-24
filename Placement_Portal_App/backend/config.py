import sqlite3
import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

WEBHOOK = "https://chat.googleapis.com/v1/spaces/AAQAg99pa4g/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=1Y0-Tl4cHVP8IaNCqutp6QsQfroOPxwK-0ou_HbhKwk"

EMAIL = "23f3002386@ds.study.iitm.ac.in"
PASSWORD = "wbxihjaamcwcszqe"

def send_reminders():
    conn = sqlite3.connect("Placement_Portal.db")
    cursor = conn.cursor()
    cursor.execute("""SELECT S.NAME, D.TITLE, D.APPLICATION_DEADLINE FROM STUDENT S JOIN APPLICATION A ON S.ID = A.STUDENT_ID JOIN DRIVE D ON D.ID = A.DRIVE_ID 
    WHERE DATE(D.APPLICATION_DEADLINE)=DATE('now','+1 day')""")
    reminders = cursor.fetchall()
    for student, title, deadline in reminders:
        message = {
            "text":
            f"""
            Student : {student}

            Drive : {title}

            Deadline : {deadline}

            Apply before the deadline.
            """
        }
        requests.post(WEBHOOK, json=message)
    conn.close()
    print("Reminder Sent")

def send_monthly_report():
    conn = sqlite3.connect("Placement_Portal.db")
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM DRIVE")
    drives = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM APPLICATION")
    applications = cursor.fetchone()[0]
    cursor.execute("""SELECT COUNT(*) FROM APPLICATION WHERE STATUS='APPROVED'""")
    selected = cursor.fetchone()[0]
    conn.close()
    html = f"""
    <html>
    <body>
    <h2>Monthly Placement Report</h2>
    <table border="1" cellpadding="10">
    <tr>
        <th>Category</th>
        <th>Count</th>
    </tr>
    <tr>
        <td>Total Drives</td>
        <td>{drives}</td>
    </tr>
    <tr>
        <td>Applications</td>
        <td>{applications}</td>
    </tr>
    <tr>
        <td>Students Selected</td>
        <td>{selected}</td>
    </tr>
    </table>
    </body>
    </html>
    """
    msg = MIMEMultipart()
    msg["From"] = EMAIL
    msg["To"] = EMAIL
    msg["Subject"] = "Monthly Placement Report"
    msg.attach(MIMEText(html, "html"))
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(EMAIL, PASSWORD)
    server.sendmail(
        EMAIL,
        EMAIL,
        msg.as_string()
    )
    server.quit()
    print("Email Sent")