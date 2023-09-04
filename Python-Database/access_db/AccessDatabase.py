import pyodbc

DRIVER_NAME = 'SQL SERVER'
SERVER_NAME = 'RICKY'
DATABASE_NAME = 'HR'

connection_str = f"""
                DRIVER={{{DRIVER_NAME}}};
                SERVER={SERVER_NAME};
                DATABASE={DATABASE_NAME};
                Trusted_Connection=yes;                
                """
conn = pyodbc.connect(connection_str)

cursor = conn.cursor()
cursor.execute('SELECT * FROM REGIONS;')

for row in cursor:
    print(row)
