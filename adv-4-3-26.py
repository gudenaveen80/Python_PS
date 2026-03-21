import mysql.connector

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'naveen@123',
    db_name = database_123
    
    )
    
cursor = conn.cursor()

cursor.execute(select * from users)

for row in rows cursor.fetchall():
    print(row)
cursor.close()
conn.close()