"""
A simple set of tests for basic functional setup and use


NOTE: Make sure that traceworker has privileges to login!
TODO: Test logging not implemented
"""
from unittest import TestCase
import logging
import logging.config
from testfixtures import LogCapture
import pandas as pd
import setup
from data.dbaccessor import DBAccessor
import xlrd
import os

class TestLittleTraseSetup(TestCase):

    def test_logging_config(self):

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
            print("TestDBAccess FAILS: Check connection string: " + setup.CONN_STRING)
            raise

class TestDBRawDataFile(TestCase):

    def test_xl_access(self):

        try:
            xlpath = os.path.join(setup.BASE_DIRECTORY,setup.XL_DATA_LOC)
            datapath = os.path.join(xlpath,setup.XL_LOOKUP_TABLES)
            xlwb = xlrd.open_workbook(datapath)
        except:
            print("TestDBRawDataFile FAILS: Check paths: ")
            print("excel data location: "+ setup.XL_DATA_LOC)
            print("excel data location: " + setup.XL_LOOKUP_TABLES)
            print("Also make sure the library 'xlrd' is correctly installed")
            raise


        xls1 = xlwb.sheet_by_name('tbl_location_type')

        # print(xls1)
        cols = []
        for i in range(xls1.ncols):
            col = str(xls1.cell(0,i).value)
            cols.append(col)

        print(cols)
        print(','.join(cols))
        tcols = '('+','.join(cols)+')'
        print(tcols)

        vals = {}
        for i in range(1, xls1.nrows):
            lval = [ ]
            for c in range(xls1.ncols):
                val = xls1.cell(i,c).value
                if isinstance(val,float):
                    val = int(val)
                lval.append(val)
                print(cols[c])
                print(val)
            vals[i] = lval
            print(lval)
        print(vals)

        # xl = pd.ExcelFile(tdata)
        #
        # print(xl.sheet_names)
        #
        # sheet1 = xl.parse(0)
        # # print(sheet1)
        # print(sheet1.columns)
        # for r in sheet1.iterrows():
        #     print(r)
        #
        # sheet2 = xl.parse(xl.sheet_names.index('tbl_municipality'))
        # # print(sheet2)
        #
        #
        # lookup_tables = [
        #     'tbl_location_type',
        #     'tbl_node_type',
        #     'tbl_company_type',
        #     'tbl_trade_entity_type',
        #
        #     'tbl_unit',
        #     'tbl_measurement_type',
        # ]
        # itable = lookup_tables.index('tbl_location_type')
        # table = xl.parse(xl.sheet_names.index(lookup_tables[itable]))
        # print(table)
        #
        # sql = "SELECT * IN %s;" % 'tbl_location_type'
        # print(sql)
        #
        # cols = ""
        # for col in table.columns:
        #     print(col)
        #     cols += col + ","
        #
        # columns = "("+cols+")"
        # print(cols)




        # df1 = xl.parse('tbl_location_type')
        #print(df1)
        # print(df1.icol(0))


        # df1 = pd.DataFrame(df1.values)
        # print(df1)
        #
        # print('printing r')
        # for r in df1:
        #
        #     print(r)


        self.assertTrue(False)



