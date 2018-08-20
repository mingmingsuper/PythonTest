import mysql.connector

config = {
    'user': 'root',
    'password': 'nishengri',
    'host': 'localhost',
    'port': '3306',
    'database': 'blog_db'
}

con = mysql.connector.connect(**config)
cursor = con.cursor()
cursor.execute('SELECT * FROM Users')
users = cursor.fetchall()
print(users)
con.commit()
cursor.close()
con.close()
