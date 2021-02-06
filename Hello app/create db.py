import psycopg2
from psycopg2 import Error


connection = psycopg2.connect(user="postgres",password="postgres",host="127.0.0.1",port="5432",database="testdb")

# Create a cursor to perform database operations
cursor = connection.cursor()

# Pass data to fill a query placeholders and let Psycopg perform
# the correct conversion (no more SQL injections!)
cursor.execute("INSERT INTO test (num, data) VALUES (%s, %s);", (200, 'b'))

# cursorQuery the database and obtain data as Python objects
cursor.execute("SELECT * FROM test;")
print(cursor.fetchall())

cursor.close()
connection.close()
