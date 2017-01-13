#!/usr/bin/python
# -*- coding: UTF-8 -*-

import thread
import time
import Queue

import fileLog
import cliLog

DEBUG   = "DEBUG"
INFO    = "INFO"
NOTICE  = "NOTICE"
WARNING = "WARNING"
ERROR   = "ERROR"
ALERT   = "ALERT"

_logQuery = Queue.Queue();

def _fnLogRuntime():
    '''
    日志线程函数
    '''
    while 1:
        '''
        1 表示阻塞等待
        5 表示最多等5秒钟
        '''
        try:
            log = _logQuery.get(1, 5);
            fileLog.write(log);
            cliLog.write(log);
        except:
            continue;

def write(level, message):
    _logQuery.put({'time': time.time(), 'level': level, 'message': str(message)})

def fnLogStart():
    thread.start_new_thread(_fnLogRuntime, ());
