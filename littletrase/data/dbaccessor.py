"""
DBAccessor

"""
import psycopg2
import setup


class DBAccessor(object):

    def __init__(self):
        self._conn = psycopg2.connect(setup.CONN_STRING)
        self._cur = self._conn.cursor()

    def close(self):
        self._cur.close()
        self._conn.close()

    def query(self, sql):
        self._cur.execute(sql)
        if self._cur.description is not None:
            return self._cur.fetchall()
        return None

