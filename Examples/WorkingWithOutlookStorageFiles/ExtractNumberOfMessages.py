from aspose.email.storage.pst import *

def run():

	dataDir = ""
	#ExStart: ExtractNumberOfMessages
	pst = PersonalStorage.from_file(dataDir + "Outlook.pst")
				
	# Get the format of the file
	inbox = pst.root_folder.get_sub_folder("Inbox")

	print("Total messges count in Inbox folder: " + str(len(inbox.get_contents())))

	# Extracts messages starting from 3rd index top and extract total 100 messages
	messagesColl = inbox.get_contents(3, 5)

	print("Total Messages: " + str(len(messagesColl)))
	#ExEnd: ExtractNumberOfMessages
	
if __name__ == '__main__':
    run()