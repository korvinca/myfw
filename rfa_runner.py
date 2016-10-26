'''
RAF
Created on Oct 20, 2016

@author: korvinca
'''

from rfa_utils import get_log, qaprint, get_log_v1


def testcase_01():
    ''' Print message in log file - logginer
    '''
    kwargs = {'log_dir': 'logs', 'log_name': 'assignment_01'}
    log = get_log(**kwargs)
    message = "It is working, right?"
    log.info(message)

def testcase_02():
    ''' Print message in log file - create file in append mode
    '''
    log = get_log_v1()
    message = "It is working, right?\n"
    qaprint(log, message)

if __name__ == '__main__':
    pass
    # testcase_01()
    # testcase_02()
