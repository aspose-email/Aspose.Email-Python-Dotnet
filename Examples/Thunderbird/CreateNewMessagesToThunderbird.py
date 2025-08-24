import aspose.email
from aspose.email.storage.mbox import MboxrdStorageWriter
from aspose.email import MailMessage

def run():
	dataDir = "Data/"
	#ExStart: CreateNewMessagesToThunderbird
	# Initialize MboxStorageWriter and pass the above stream to it
	#writer =MboxrdStorageWriter(dataDir + "ExampleMBox_out.mbox", False)
	# Prepare a new message using the MailMessage class
	message = MailMessage("from@domain.com", "to@domain.com", "Eml generated for Mbox", "added from Aspose.Email for Python")
	message.is_draft = False
	# Add this message to storage
	with MboxrdStorageWriter(dataDir + "ExampleMBox_out.mbox", False) as writer:
		writer.write_message(message)
	#ExEnd: CreateNewMessagesToThunderbird

if __name__ == '__main__':
    run()
