from datetime import datetime

def my_scheduled_job():
    myFile = open('cron_log.txt', 'a') 
    myFile.write('\nAccessed on ' + str(datetime.now()))
    print('Hello World')