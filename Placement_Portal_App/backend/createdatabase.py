import sqlite3

from models.admin import create_admin_table
from models.student import create_student_table
from models.company import create_company_table
from models.application import create_application_table
from models.drive import create_drive_table

create_admin_table()
create_student_table()
create_company_table()
create_application_table()
create_drive_table()