#!/usr/bin/env python

import sys, configparser

config = configparser.ConfigParser()
config.readfp(sys.stdin)

print("declare -a SERVICES")
print("declare -a SERVICE_NAMES")
for sec in config.sections():
    print("SERVICES+=('%s@%s')" % (sec, config.get(sec, 'version')))
    print("SERVICE_NAMES+=('%s')" % (sec))
