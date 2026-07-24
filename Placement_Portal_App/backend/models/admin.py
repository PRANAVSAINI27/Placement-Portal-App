import sqlite3

def create_admin_table():
    conn = sqlite3.connect('Placement_Portal.db')
    cursor = conn.cursor()
    
    cursor.execute('''CREATE TABLE ADMIN(ID VARCHAR PRIMARY KEY UNIQUE NOT NULL, NAME VARCHAR NOT NULL, PASSWORD VARCHAR NOT NULL)''')
    cursor.execute('''INSERT INTO ADMIN VALUES("Admin","ADMIN","Admin@123")''')
    
    conn.commit()
    conn.close()
    
