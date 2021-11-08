#!/usr/bin/env bash

from crontab import CronTab

cron = CronTab(user='chavez')

task = cron.new(command='cd /Users/chavez/Desktop/Creative Work/repos/python-crontab/pycrontab/api/ && /Users/chavez/Desktop/Creative Work/repos/python-crontab/venv/bin/python /Users/chavez/Desktop/Creative Work/repos/python-crontab/pycrontab/api/python_script.py') 

task.minute.every(1)

cron.write()
 