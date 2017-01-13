#!/usr/bin/python
# -*- coding: UTF-8 -*-
#
#

import sys
import os

sys.path.append('../')

import log
import globals

configPath = './conf'

def _readConfig(file):
    lines   = []
    config  = {}

    try :
        handle = open(file, "rw+")
    except :
        return {}
    else :
        try:
            lines = handle.readlines();
        except:
            return {}
        finally:
            handle.close()

    for line in lines:
        line = line.strip()
        if len(line) <= 0:
            continue;

        if line[0:1] == "#" :
            continue;

        try :
            pos = line.index("=")
        except:
            continue;

        if pos <= 0:
            continue;

        key = line[ 0 : pos ]
        val = line[ pos + 1 :  ]
        key = key.strip()
        val = val.strip()
        config[key] = val

    return config

def load():
    global configs
    files = os.listdir(configPath)
    for confFile in files:
        pos = confFile.index(".")
        if pos < 0:
            continue

        suffix = confFile[pos+1: ]
        if len(suffix) <= 0 or cmp(suffix, 'conf') > 0:
            continue

        name = confFile[0: pos]
        if len(name) <= 0:
            continue;

        log.write(log.INFO, "Read conf from file " + name);

        conf = _readConfig(configPath + "/" + confFile)

        globals.configs[name] = conf
