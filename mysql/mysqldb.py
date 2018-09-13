import MySQLdb.cursors

DBCONF = {
    'host': 'localhost',
    'port': 3306,
    'user': 'lee',
    'passwd': 'lee',
    'db': 'sandbox',
    'charset': 'utf8mb4',
    'autocommit': True,
    'cursorclass': MySQLdb.cursors.DictCursor
}

conn = MySQLdb.connect(**DBCONF)

cur = conn.cursor()
cur.execute('SELECT id, name, created_at FROM users')
print(cur.fetchall())

conn.close()
