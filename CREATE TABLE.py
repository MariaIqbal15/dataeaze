import mysql.connector
conn=mysql.connector.connect(
    host='localhost',
    password='a1!@',
    user='root',
    database='db1'
    )
cur=conn.cursor()
s="CREATE TABLE book(bookid integer(4),title varchar(20),price float(5,2))"
cur.execute(s)
