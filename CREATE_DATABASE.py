import mysql.connector
conn=mysql.connector.connect(host='localhost',password='a1!@',user='root')
cur=conn.cursor()
cur.execute("CREATE DATABASE db1")
