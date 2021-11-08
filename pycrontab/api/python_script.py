#!/usr/bin/env bash

from datetime import datetime

myFile = open('/Users/chavez/Desktop/Creative Work/repos/python-crontab/pycrontab/api/cron_log.txt', 'a') 
myFile.write('\nAccessed on ' + str(datetime.now()))