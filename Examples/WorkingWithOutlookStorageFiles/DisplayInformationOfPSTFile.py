from aspose.email.storage.pst import *
from aspose.email.mapi import MapiCalendar
from aspose.email.mapi import MapiRecipientType
from aspose.email.mapi import MapiRecipientCollection
from aspose.email.mapi import MapiRecipient

import datetime as dt
from datetime import timedelta

import os

def run():
	dataDir = "Data/"
	#ExStart: DisplayInformationOfPSTFile
	personalStorage = PersonalStorage.from_file(dataDir + "Outlook.pst")

	folderInfoCollection = personalStorage.root_folder.get_sub_folders()

	for folderInfo in folderInfoCollection:

		print("Folder: " + folderInfo.display_name)
		print("Total Items: " + str(folderInfo.content_count))
		print("Total Unread Items: " + str(folderInfo.content_unread_count))
		print("----------------------")
	#ExEnd: DisplayInformationOfPSTFile
	
if __name__ == '__main__':
    run()
