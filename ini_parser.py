#!/usr/bin/env python

import sys, ConfigParser

config = ConfigParser.ConfigParser()
config.readfp(sys.stdin)

print "declare -a SERVICES"
for sec in config.sections():
    print "SERVICES+=('%s')" % (sec)
    print "declare -a %s" % (sec)
    for key, val in config.items(sec):
        print '%s[%s]="%s"' % (sec, key, val)
