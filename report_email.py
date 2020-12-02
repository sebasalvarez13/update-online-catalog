#!/usr/bin/env python3

import reports
import datetime
import os
import sys
import emails

def process_data():
    src_folder = "/home/student-02-0680a0f6b364/supplier-data/descriptions/"
    description_files = os.listdir(src_folder)
    summary = ""
    for file in description_files:
        with open(src_folder + file, "r") as open_description:
            reader = open_description.read().split("\n")
            summary += "name: " + reader[0] + "<br/>" +  "weight: " + reader[1] + "<br/><br/>"

    return(summary)


def main(argv):
    content = process_data()
    #summary = "data fruits goes here"
    today = datetime.datetime.today()
    title = "Process update on " + today.strftime("%B %d, %Y")
    #turns info into a PDF report_title
    reports.generate_report("/tmp/processed.pdf", title, content)

    #send PDF report as an email attachment
    sender = "automation@example.com"
    receiver = "student-02-0680a0f6b364@example.com"
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    message = emails.generate_email(sender, receiver, subject, body, "/tmp/processed.pdf")
    emails.send_email(message)

if __name__ == "__main__":
    main(sys.argv)
