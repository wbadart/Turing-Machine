#!/usr/bin/env python

'''
' tm.py
'
' Driver file to test Turing Machine
' class defined in lib.py.
'
' Will Badart
' NOV 2016
'''

import sys
from getopt import getopt
from lib import TM

#####################
# Help function to give instructions for driver
# None usage(status:int)
#####################

def usage(status=0):
    print >>(sys.stdout if not status else sys.stderr),\
            '''usage: {} DEFN_FNAME TEST_FNAME [ -h ]
    DEFN_FNAME     Name of file containing TM definition
    TEST_FNAME     Name of file containing test strings
    -h             Show this help message'''\
            .format(sys.argv[0])
    sys.exit(status)


#####################
# Error function to handle error reporting and exiting
# None error(msg:str, status:int)
#####################

def error(msg, status=1):
    print >>sys.stderr, 'ERROR: {}'.format(msg)
    usage(status)


#####################
# Wrap the vanilla open statement in try/catch
# file try_read(fname:str)
#####################

def try_read(fname):
    try:
        return open(fname, 'r')
    except IOError as e:
        error(e)


#####################
# MAIN EXECUTION
#####################

# Check for main execution to prevent local variables
#   from being visible during export
if __name__ == '__main__':

    # Parse command line options
    try:
        opts, args = getopt(sys.argv[1:], 'h', ['help'])
    except Exception as e:
        error(e)
    for o, a in opts:
        if o == '-h' or o == '--help':
            usage()

    # Sanity checks:
    #   User must provide exactly two arguments
    if len(args) != 2:
        error('Must provide DEFN_FNAME and TEST_FNAME')

    #   Both file names must be given
    if not args[0] or not args[1]:
        error('DEFN_FNAME and TEST_FNAME cannot be empty')

    DEFN_FNAME = args[0]
    TEST_FNAME = args[1]
    
    # Run construction and test
    #   try_read catches IOErrors (eg file doesn't exist)
    uut = TM(try_read(DEFN_FNAME))
    uut.test(try_read(TEST_FNAME))

