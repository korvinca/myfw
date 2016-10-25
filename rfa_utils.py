'''
RAF
Created on Oct 20, 2016

@author: korvinca
'''


import datetime
import time
import logging
import os
import traceback


def get_log(log_dir=None, log_name=None):
    """ Create handler for log file
    """

    if not log_dir:
        log_dir = '.'
    else:
        dir_create(log_dir)

    if not log_name:
        log_name = "testrun"

    try:
        log = logging.getLogger()
        log.setLevel(logging.INFO)
        hdlr = logging.FileHandler(os.path.join(log_dir + '/' + log_name +
                                                "_%s.log" % get_cur_time()))
        formatter = logging.Formatter('%(asctime)s %(filename)s '
                                      '[LINE %(lineno)d] %(levelname)s: '
                                      '%(message)s')
        hdlr.setFormatter(formatter)
        log.addHandler(hdlr)
        handler_stream = logging.StreamHandler()
        handler_stream.setFormatter(formatter)
        handler_stream.setLevel(logging.INFO)
        log.addHandler(handler_stream)
    except OSError as err:
        print err
        return -1
    return log

def get_log_v1(log_dir=None, log_name=None):
    """ creates a log file and returns file handler
    """

    if not log_dir:
        log_dir = '.'
    else:
        dir_create(log_dir)

    if not log_name:
        log_name = "testrun"

    try:
        date_time = str(get_cur_time())
        logname = "_".join([log_name, date_time]) + ".log"
        log_full_name = os.path.join(log_dir, '/', logname)
        log = open(log_full_name, "a")
    except OSError as err:
        print err
        # traceback.print_exc()
        return False
    return log

def get_cur_time(sec=None):
    """ Return time stamp as string
    """
    if not sec:
        time_str = datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d_%H%M')
    else:
        time_str = datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d%_H%M%S')
    return str(time_str)

def dir_create(dirname):
    """ Create a new directory
    """
    if not os.path.isdir(dirname):
        try:
            os.makedirs(dirname)
        except OSError as err:
            print err
            traceback.print_exc()
            return exit(1)

