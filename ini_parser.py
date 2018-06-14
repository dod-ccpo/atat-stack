#!/usr/bin/env python

import sys, ConfigParser

config = ConfigParser.ConfigParser()
config.readfp(sys.stdin)

print "declare -a SERVICES"
for sec in config.sections():
    print "SERVICES+=('%s@%s')" % (sec, config.get(sec, 'version'))
