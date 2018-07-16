import aspose.email
from aspose.email.clients.imap import ImapClient
from aspose.email.clients import SecurityOptions
from aspose.email import MailMessage

def run():
	dataDir = "Data/"

	try:
	#ExStart: AppendMessagetoFolder
		with ImapClient("imap.gmail.com", 993, "username", "password") as client:
			client.select_folder("Inbox")
			msg = MailMessage("user@domain1.com", "user@domain2.com", "subject", "message")
			client.subscribe_folder(client.current_folder.name)        
			client.append_message(client.current_folder.name, msg)
	 #ExEnd: AppendMessagetoFolder    
	except Exception as ex:
		print(str(ex))

if _name_ == '__main__':
    run()