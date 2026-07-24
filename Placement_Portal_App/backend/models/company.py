import sqlite3

def create_company_table():
    conn = sqlite3.connect('Placement_Portal.db')
    cursor = conn.cursor()
    
    cursor.execute('''CREATE TABLE COMPANY(ID INTEGER PRIMARY KEY AUTOINCREMENT, NAME VARCHAR NOT NULL UNIQUE, 
                  HR_CONTACT INTEGER(10) NOT NULL UNIQUE, WEBSITE VARCHAR NOT NULL, PASSWORD VARCHAR NOT NULL, APPROVAL_STATUS VARCHAR NOT NULL DEFAULT 'PENDING', 
                  STATUS VARCHAR NOT NULL DEFAULT 'ACTIVATED')''')
    
    conn.commit()
    conn.close()
    
