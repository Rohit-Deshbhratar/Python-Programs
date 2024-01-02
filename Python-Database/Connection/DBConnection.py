import pyodbc

class DBConnection:
    connection_string = ""
    
    def __init__(self):
        self.DRIVER_NAME = 'SQL SERVER'
        self.SERVER_NAME = 'ROHIT'
        self.DATABASE_NAME = 'BikeStores'
    
    def connection(self):
        self.connection_string = f"""
                DRIVER={{{self.DRIVER_NAME}}};
                SERVER={self.SERVER_NAME};
                DATABASE={self.DATABASE_NAME};
                Trusted_Connection=yes;                
                """
        conn = pyodbc.connect(self.connection_string)
        print("Connected successfully...")
        return conn

    

def main():
    dbconnection = DBConnection()
    dbconnection.connection()

main()
    
