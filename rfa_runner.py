'''
RAF
Created on Oct 20, 2016

@author: korvinca
'''

from rfa_utils import get_log


def testcase_01():
    ''' Print message in log file - Assignment 01
    '''
    log_dir = 'logs'
    test_name = 'assignment_01'
    log = get_log(log_dir, test_name)
    # Write message in log file
    message = "It is working, right?"
    log.info(message)


if __name__ == '__main__':
    testcase_01()
