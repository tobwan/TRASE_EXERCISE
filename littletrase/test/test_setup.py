"""
A simple set of tests for basic functional setup and use


NOTE: Make sure that traceworker has privileges to login!
"""
from unittest import TestCase
import logging
import logging.config
from testfixtures import LogCapture
import psycopg2
from psycopg2 import sql
import setup
from data.dbaccessor import DBAccessor


class TestLittleTraseSetup(TestCase):

    def testLoggingConfig(self):

        logging.config.dictConfig(setup.LOGGING)
        logger = logging.getLogger('root')

        with LogCapture() as l:
            logger.debug('debug msg')
            l.check(
                ('root', 'DEBUG', 'debug msg')
            )

            try:
                l.check(
                  ('BAD_LOGGER_NAME', 'DEBUG', 'debug msg')
                )
            except AssertionError:
                pass

class TestDBAccess(TestCase):

    def test_connection(self):
        try:
            db = DBAccessor()
            SQL = "SELECT 1;"
            result = db.query(SQL)
            self.assertEqual(result,[(1,)])
        except:
            print("Check connection string: " + setup.CONN_STRING)
            raise



