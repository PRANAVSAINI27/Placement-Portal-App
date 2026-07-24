import sqlite3

def create_student_table():
    conn = sqlite3.connect('Placement_Portal.db')
    cursor = conn.cursor()
    
    cursor.execute('''CREATE TABLE STUDENT(ID VARCHAR PRIMARY KEY NOT NULL UNIQUE, NAME VARCHAR NOT NULL, 
                   BRANCH VARCHAR NOT NULL, CONTACT_NUMBER INTEGER(10) NOT NULL UNIQUE,CGPA DECIMAL(2,1) NOT NULL, 
                   YEAR INTEGER NOT NULL,APPROVAL_STATUS VARCHAR NOT NULL DEFAULT 'PENDING', STATUS VARCHAR NOT NULL DEFAULT 'ACTIVATED', 
                   PASSWORD VARCHAR NOT NULL)''')
    
    conn.commit()
    conn.close()
    
