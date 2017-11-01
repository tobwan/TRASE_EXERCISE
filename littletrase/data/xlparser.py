"""

"""
import xlrd
import os
import setup

class XLParser(object):

    def __init__(self):
        dpath = os.path.join(setup.BASE_DIRECTORY, setup.RAW_DATA_LOC)
        tdata = os.path.join(dpath, 'trase-tbl-data.xlsx')
        self.xlwb = xlrd.open_workbook(tdata)
        # xls1 = xlwb.sheet_by_name('tbl_location_type')

    def parsetable(self,table):
        dvals = {}

        return dvals