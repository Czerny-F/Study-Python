import time
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


def routine():
    conn = MySQLdb.connect(**DBCONF)

    cur = conn.cursor()
    cur.execute('SELECT id, name, created_at FROM users')
    cur.fetchall()

    conn.close()


start = time.time()
for _ in range(1000):
    routine()

print('elapsed time: {0:.4f}[sec]'.format(time.time() - start))
