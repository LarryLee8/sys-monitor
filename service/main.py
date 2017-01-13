#!/usr/bin/python
# -*- coding: UTF-8 -*-

import log
import conf
import time

import globals

if __name__ == "__main__":
    log.fnLogStart();

    log.write(log.DEBUG, "Load configurations")
    conf.load()
    log.write(log.NOTICE, "Load configuration finished " + str(globals.configs))

    time.sleep(2)
