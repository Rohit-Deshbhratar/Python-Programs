import cx_Oracle


# Access a table in Oracle database
try:
 
    con = cx_Oracle.connect('HR/HR@localhost:1521/xe')
    print(con.version)
 
    # Now execute the sqlquery
    curs = con.cursor()
 
    # Creating a table employee
    curs.execute("SELECT * FROM REGIONS")
    rows = curs.fetchall()
    print(rows)
 
except cx_Oracle.DatabaseError as e:
    print("There is a problem with Oracle", e)
 
# by writing finally if any error occurs
# then also we can close the all database operation
finally:
    if curs:
        curs.close()
    if con:
        con.close()
