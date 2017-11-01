"""
LittleTrase Exercise

Run the program from here.
"""

import logging
import logging.config
import os
import setup


def main():

    logging.config.dictConfig(setup.LOGGING)
    logger = logging.getLogger('root')

    dir_path = os.path.dirname(os.path.realpath(__file__))
    print(dir_path)

    f=open('test.csv','r')
    print(f.read())

    fpath = dir_path + '\\thing.csv'
    f = open(fpath,'r')
    print('hello')

    f.read()
    print(f.read())

if __name__ == "__main__":
    main()


