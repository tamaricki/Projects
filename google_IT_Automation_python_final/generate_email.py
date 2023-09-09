#! usr/bin/env python3


# and the file path of the PDF to be generated as the attachment argument 
# (use ‘/tmp/processed.pdf')
#Once you define the generate_email and send_email methods, 
# call the methods under the main method after creating the PDF report:



import os
import reports
import emails
from datetime import date


text_path ='/supplier-data/descriptions/'

text = []
body_report = []
for t in os.listdir(text_path):
    with open(text_path+t, 'r') as x:
        text.append([a.strip() for a in x.readlines()]) #or text.append(x.readlines())

def body_text_data(data):
    for t in data:
        body_report.append("name: {}<br/>weight: {}\n".format(t[0], t[1]))
    return body_report

if __name__ =="__main__":

    data = body_text_data(text)
    summary = "<br/>".join(data)
    title = "Processed update {}".format(date.today())
    filename ='/tmp/processed.pdf'
    pdf = report.generate_report(filename, title, summary)
    #generate email
    sender = 'automation@example.com'
    reciever = '{}@example.com'.format(os.environ.get('USER')) # replace username with Student.... username 
    subject = 'Upload Completed - Online Fruit Store'
    body = 'All fruits are uploaded to our website successfully. A detailed list is attached to this email.'
    message = emails.generate(sender, receiver, body, filename)
    emails.send(message)
    
