"""

"""
import xlrd
import os
import logging
import setup
from data.sqlparser import SQLParser

class XLParser(object):

    def __init__(self):

        self.logger = logging.getLogger(__name__)
        self.logger.info("Create XLParser")

        try:
            self.logger.info(" Open Excel lookup data")
            dpath = os.path.join(setup.BASE_DIRECTORY, setup.XL_DATA_LOC)
            tdata = os.path.join(dpath, setup.XL_LOOKUP_TABLES)
            self.xlwb = xlrd.open_workbook(tdata)
            self.lookup_tables = self.xlwb.sheet_names()

            # self.lookups = self.logger.debug(self.xlwb.sheet_names())
        except AttributeError as e:
            self.logger.error("AttributeError: XLParser failed to initialize, check excel tests.")
            raise

        self.logger.info("Create SQLParser")
        self.sqlparser = SQLParser()


    def parse_table(self,xlsheet):
        self.logger.info("Parsing table - '%s'", xlsheet.name)

        cols = []
        for i in range(xlsheet.ncols):
            col = str(xlsheet.cell(0,i).value)
            cols.append(col)

        vals = {}
        for i in range(1, xlsheet.nrows):
            lval = []
            for c in range(xlsheet.ncols):
                val = xlsheet.cell(i,c).value
                if isinstance(val,float):
                    val = int(val)
                    val = str(val)
                lval.append(val)
            values_string = '(' + ','.join(map(str, lval)) + ')'
            vals[i] = values_string

        cols = '(' + ','.join(map(str, cols)) + ')'

        # self.logger.debug(vals)
        # self.logger.debug(cols)

        return cols,vals

    def load_lookup_tables(self):
        self.logger.info("Loading the lookup tables")

        values = {}
        columns = ""
        sql_insert_queries = {}
        for lookup_table in self.lookup_tables:
            xlsheet = self.xlwb.sheet_by_name(lookup_table)
            columns,values = self.parse_table(xlsheet)

            self.logger.info("TABLE: " + lookup_table + " " + columns)
            self.logger.info("VALUES: " + str(values))
            table_inserts = []
            for key in values.keys():
                data = {
                    'name': lookup_table,
                    'cols': columns,
                    'value': values[key]
                }
                insert_query = self.sqlparser.table_insert_query(data)
                table_inserts.append(insert_query)
                self.logger.debug(insert_query)
            sql_insert_queries[lookup_table] = table_inserts
        return sql_insert_queries