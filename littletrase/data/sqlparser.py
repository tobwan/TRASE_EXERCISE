"""
SQLParser

Creates the various queries to be run.

TODO: table_insert_query - multiple value insert option
"""
import logging


class SQLParser(object):

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def table_insert_query(self, data):
        query = "INSERT INTO %(name)s %(cols)s VALUES %(value)s;" % data
        return query
