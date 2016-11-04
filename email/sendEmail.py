import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import config

# your email address and password will be fetched from the config file

print(config.config['senderEmail'])

# fetch from the csv file

personName = ""
personEmail = ""
companyName = ""

# attachment
filename = config.config['filename']
attachment = open(config.config['attachment'], "rb")



def sendEmail(toaddr,fromEmail,name,companyName,filename,attachment):

	# to email address
	# fetch from the csv file

	subject = config.config['subject']
	subject = subject + companyName

	# create message
	msg = MIMEMultipart()
	 
	msg['From'] = fromEmail
	msg['To'] = toaddr
	msg['Subject'] = subject


	body = "Hello " + name +",\n\n"

	body = body + config.config['body']

	signature = config.config['signature']

	body = body + signature
	 
	try:
		msg.attach(MIMEText(body, 'plain'))
		 
		 
		part = MIMEBase('application', 'octet-stream')
		part.set_payload((attachment).read())
		encoders.encode_base64(part)
		part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
		 
		msg.attach(part)
		 
		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.starttls()
		server.login(fromEmail, config.config['password'])
		text = msg.as_string()
		server.sendmail(fromEmail, toaddr, text)
		server.quit()
		print("Email sent to " + name)

	except Exception, e:
		print e

"""
method parameters:
1. toaddr: address of the recipient
2. fromEmail : email address of sender
3. name : Name of the person (Receiver),
4. companyName : Company Name of the receiver,
5. filename : file name to attach
6. attachment : attachment name
"""

sendEmail("ssingh25@ncsu.edu",config.config['senderEmail'],"Nikhil","NC State",filename,attachment)