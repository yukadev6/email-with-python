import imaplib
import getpass
import email

# connect to imap server
M = imaplib.IMAP4_SSL('imap.gmail.com')

user = input("Enter your email: ")
password = getpass.getpass("Password: ")

M.login(user,password)
# method that will list everything you can check in your email
M.list()
# connect to inbox
M.select('inbox')

# use special syntx code to search email for specific parameters and get the email id from 'data'
typ, data = M.search(None,'SUBJECT "Hello"')

# pass in the protocol for fetching specific email id 
result, email_data = M.fetch(data[0],"(RFC822)")

raw_email = email_data[0][1]
raw_email_string = raw_email.decode('utf-8')
email_message = email.message_from_string(raw_email_string)

for part in email_message.walk():
	if part.get_content_type() == 'text/plain':
		body = part.get_payload(decode=True)
		print(body)


