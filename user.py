from ast import stmt
import psycopg2


try:
    conn = psycopg2.connect("dbname='testdb' user='testuser' host='localhost' password='testpw'")
except:
    print("I am unable to connect to the database")

cur = conn.cursor()

try:
    print('WARUM=!')
    cur.execute("INSERT INTO users(firstname, lastname, username, email) VALUES (%s,%s,%s,%s)", 
('test', 'dummy', 'testdummy', 'test@dum.my'))
except Exception as err:
    print('WARUM=!')
    print(err)


cur.execute("SELECT * FROM users")
x = cur.fetchall()

for i in range(len(x)):
    print(x[i])

cur.close()