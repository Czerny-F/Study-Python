import pymysql.cursors

DBCONF = {
    'host': 'localhost',
    'port': 3306,
    'user': 'lee',
    'password': 'lee',
    'db': 'sandbox',
    'charset': 'utf8mb4',
    'autocommit': True,
    'cursorclass': pymysql.cursors.DictCursor
}

conn = pymysql.connect(**DBCONF)

cur = conn.cursor()
cur.execute('SELECT id, name, created_at FROM users')
print(cur.fetchall())

conn.close()
