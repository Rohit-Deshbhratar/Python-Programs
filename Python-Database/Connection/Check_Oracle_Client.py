import cx_Oracle
import sys
import os

try:
    if sys.platform.startswith("win64"):
        lib_dir=r"C:\oraclexe\instantclient_11_2"
        cx_Oracle.init_oracle_client(lib_dir=lib_dir)
        print("WIN64")
    elif sys.platform.startswith("win32"):
        lib_dir=r"C:\oraclexe\instantclient_11_2"
        cx_Oracle.init_oracle_client(lib_dir=lib_dir)
        print("WIN32")
except Exception as err:
    print("Whoops!")
    print(err)
    sys.exit(1)