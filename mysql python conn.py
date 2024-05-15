import mysql.connector
conn=mysql.connector.connect(host='localhost',password='a1!@',user='root')

if conn.is_connected():
    print("Connection established...")
