#!/usr/bin/env python3

import shutil
import psutil
import os
import sys
import socket
import emails

def cpu_usage():
    max_usage = 80
    cpu_usage = psutil.cpu_percent(interval = 1)
    if cpu_usage > max_usage:
            return True
    return False

def disk_space():
    disk_space = psutil.disk_usage("/")
    #I want to look at free space percentage
    free_space = disk_space.free / disk_space.total * 100
    #this is the minimum percentage of disk space allowed
    min_space = 20
    if free_space < min_space:
            return True
    return False

def memory_space():
    #this is the minimum amount of memory space allowed
    min_memory = 500 *1024 * 1024 #500MB
    memory = psutil.virtual_memory()
    if memory.available < min_memory:
            return True
    return False

def localhost_resolve():
    try:
        socket.gethostbyname("127.0.0.1")
        return False
    except:
        return True

def main(argv):
    #define error messages for each of the health conditions
    conditions = [(cpu_usage, "Error - CPU usage is over 80%"), (disk_space, "Error - Available disk space is less than 20%"),
    (memory_space, "Error - Available memory is less than 500MB"), (localhost_resolve, "Error - localhost cannot be resolved to 127.0.0.1")]
    subject_message = ""
    for check, message in conditions:
        if check():
            subject_message = message

    #define email information
    sender = "automation@example.com"
    receiver = "student-02-0680a0f6b364@example.com"
    subject = subject_message
    body = "Please check your system and resolve the issue as soon as possible."
    message = emails.generate_email_error(sender, receiver, subject, body)
    emails.send_email(message)

if __name__ == "__main__":
    main(sys.argv)
