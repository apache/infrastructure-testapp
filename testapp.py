#!/usr/bin/env python3
""" Super simple test application for pipservice installer """
import certifi    # Testing pipenv installed the mods
import netaddr    # Testing more...
import time
import asfpy.syslog

print = asfpy.syslog.Printer(identity='testApp')

print("This works!")
while True:
    time.sleep(60)
    print("test app still works!")
