#! usr/bin/env python3


# #Report an error if CPU usage is over 80%
#Report an error if available disk space is lower than 20%
#Report an error if available memory is less than 500MB
#Report an error if the hostname "localhost" cannot be resolved to "127.0.0.1"
#script needs to run every 60 seconds but, not sure if this should bee implemented time? 

import psutil
import shutil
from emails import generate_error_report , send
import socket
import os
 

def cpu_usage():
    usage = psutil.cpu_percent()
    return usage < 80 #normal should be True


def disk_usage(disk):
    total, used, free=shutil.disk_usage(disk)
    percent = round((free/total)*100,2)
    return percent > 20 #normal should be True

def available_memory():
    mem = psutil.virtual_memory()[1]/(1024*1024)
    return mem>500  #usually should be True

def hostname_check():
    host = socket.gethostbyname("localhost")
    return host=="127.0.0.1"  #should be usually True



check_funcs= [(cpu_usage(),'Error - CPU usage is over 80%'), 
             (disk_usage('/'), 'Error - Available disk space is lower than 20%'),
             (available_memory(), 'Error - Available memory is less than 500MB'), 
             (hostname_check(), 'Error - localhost cannot be resolved to 127.0.0.1')]

error = False
for function, message in check_funcs:
    if not function:
        error_message = message
        error = True
if error:
            #print(error_message)
    s = 'automation@example.com'
    r = '{}@example.com'.format(os.environ.get('USER')) # replace with student ID
    subject = error_message
    body = 'Check your system and resolve the issue as soon as possible!'
    message = generate_error_report(s, r, subject, body)
    send(message)
         
