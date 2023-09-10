import pymssql

class Connection:
    conn = ""

    def __init__(self):    
        self.conn = pymssql.connect(
            server='RICKY',
            database='ETL',
            as_dict=True
        )

    def create_table(self, table_name, schema):
        create_query = "CREATE TABLE {0}({1})".format(table_name, schema)
        cursor = self.conn.cursor()
        cursor.execute(create_query)
        self.conn.commit()
        print("Table is created...")
    
    def insert_table(self, table_name, schema, values):
        st = schema.split(',')
        st1 = ""
        #print(st)
        for i in st:
            b = i.split(" ")
            st1 = st1+b[0]+','
        schema = st1[:len(st1) - 1]
        print(schema)
        insert_query = "INSERT INTO {0}(PRODUCT_ID,PRODUCT_NAME,PRICE) VALUES({2})".format(table_name, schema, values)
        cursor = self.conn.cursor()
        cursor.execute(insert_query)
        self.conn.commit()
        print("Row is inserted...")
    
    def select(self, table_name, select_columns):
        select_query = "SELECT {1} FROM {0}".format(table_name, select_columns)
        cursor = self.conn.cursor()
        cursor.execute(select_query)
        row = cursor.fetchall()
        for i in row:
            print(f"{i['PRODUCT_ID']}\t{i['PRODUCT_NAME']}\t{i['PRICE']}")
        print("Table is selected...")
    
    def update(self, table_name, set_condition, filter_condition):
        update_query = "UPDATE {0} SET {1} WHERE {2}".format(table_name, set_condition, filter_condition)
        cursor = self.conn.cursor()
        cursor.execute(update_query)
        self.conn.commit()
        print("Table is updated...")
    
    def delete(self, table_name, delete_condition):
        delete_query = "DELETE FROM {0} WHERE {1}".format(table_name, delete_condition)
        cursor = self.conn.cursor()
        cursor.execute(delete_query)
        self.conn.commit()
        print("Row is deleted...")

connection = Connection()
table_name = "GROCERRY"
schema = """
            PRODUCT_ID INT,
            PRODUCT_NAME VARCHAR(50),
            PRICE DECIMAL(4,2)"""
values = "3, 'Poha', 84"
select_columns = "PRODUCT_ID,PRODUCT_NAME,PRICE"
set_condition = "PRODUCT_ID = 4"
filter_condition = "PRODUCT_NAME = 'Poha'"
delete_condition = "PRODUCT_ID=4"
#connection.create_table(table_name, schema)
#connection.insert_table(table_name, schema, values)
#connection.update(table_name, set_condition, filter_condition)
#connection.delete(table_name, delete_condition)
connection.select(table_name,select_columns)

# query = "SELECT * FROM REGIONS;"

# cursor = conn.cursor()
# cursor.execute(query)

# records = cursor.fetchall()
# for r in records:
#     print(f"{r['region_id']}\t{r['region_name']}")

