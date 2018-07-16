from aspose.email.storage.pst import *
from aspose.email.mapi import MapiMessage
from aspose.email import License



	# Recursive method to traverse through all folders of a PST
	def DisplayFolderContents(folderInfo, pst):
		print("Folder: " + folderInfo.display_name)

		print("==================================");

		# Display information about messages inside this folder
		messageInfoCollection = folderInfo.get_contents()

		for messageInfo in messageInfoCollection:
			print ("Subject: " + messageInfo.subject)
			print("To: " + messageInfo.display_to)

		if folderInfo.has_sub_folders is True:
			for subFolderInfo in folderInfo.get_sub_folders():
				DisplayFolderContents(subFolderInfo, pst)

def run():					
	dataDir = ""

	#ExStart: GetMessagesInformation
	#Read PST file and recursively list its contents
	pst = PersonalStorage.from_file(dataDir + "Outlook.pst")

	folderInfo = pst.root_folder

	DisplayFolderContents(folderInfo, pst)
	#ExEnd: GetMessagesInformation
	
if __name__ == '__main__':
    run()