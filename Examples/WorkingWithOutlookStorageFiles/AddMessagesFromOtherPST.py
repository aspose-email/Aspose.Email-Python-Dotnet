from aspose.email.storage.pst import *
from aspose.email.mapi import MapiMessage

def run():
	dataDir = ""
	#ExStart: AddMessagesFromOtherPST
	sourcePst = PersonalStorage.from_file(dataDir + "Outlook.pst")

	# Add new folder "Inbox"
	sourceFolder = sourcePst.root_folder.get_sub_folder("Inbox")

	destPst = PersonalStorage.create("DestinationPst_out.pst", FileFormatVersion.UNICODE)

	# Add new folder "Inbox"
	destFolder = destPst.root_folder.add_sub_folder("Inbox")

	sourceMsgs = sourceFolder.get_contents()

	destFolder.add_messages(sourceFolder.enumerate_mapi_messages())

	#Verify that the messages have been added to the destination PST
	print(str(destFolder.content_count))
	#ExEnd: AddMessagesFromOtherPST
	
if __name__ == '__main__':
    run()