import time
from functools import partial
from sqlalchemy import create_engine
import MySQLdb.cursors

SCHEME = 'mysql://{user}:{passwd}@{host}/{db}'.format(
    user='lee', passwd='lee', host='localhost', db='sandbox'
)
DBCONF = {
    'charset': 'utf8mb4',
    'autocommit': True,
}

engine = create_engine(SCHEME, connect_args=DBCONF)


def routine():
    conn = engine.raw_connection()
    conn.cursor = partial(conn.cursor, MySQLdb.cursors.DictCursor)

    cur = conn.cursor()
    cur.execute('SELECT id, name, created_at FROM users')
    cur.fetchall()

    conn.close()


start = time.time()
for _ in range(1000):
    routine()

print('elapsed time: {0:.4f}[sec]'.format(time.time() - start))
