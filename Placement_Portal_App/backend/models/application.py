import sqlite3

def create_application_table():
    conn = sqlite3.connect('Placement_Portal.db')
    cursor = conn.cursor()
    
    cursor.execute('''CREATE TABLE APPLICATION(ID INTEGER PRIMARY KEY AUTOINCREMENT, STUDENT_ID VARCHAR NOT NULL, 
                   DRIVE_ID INTEGER NOT NULL, APPLICATION_DATE DATE NOT NULL, STATUS VARCHAR NOT NULL DEFAULT 'PENDING', 
                   FOREIGN KEY(STUDENT_ID) REFERENCES STUDENT(ID), FOREIGN KEY(DRIVE_ID) REFERENCES DRIVE(ID))''')
    
    conn.commit()
    conn.close()
    
