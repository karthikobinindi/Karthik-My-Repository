import mysql.connector

host = "localhost"
user = "root"
password = "root123"
database = "feb26"

conn = mysql.connector.connect(host=host, user=user, password=password, database=database)
cursor = conn.cursor()
print("connected to the database successfully")
query = "SELECT * FROM feb26.employee"
cursor.execute(query)

result = cursor.fetchall()

for row in result:
    print(row)
