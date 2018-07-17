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
	#ExStart: SaveCalendarItems
	personalStorage = PersonalStorage.from_file(dataDir + "AddMapiCalendarToPST_out.pst")

	calFolder = personalStorage.get_predefined_folder(StandardIpmFolder.APPOINTMENTS)

	print("Total items: " + str(calFolder.content_count))

	for messageInfo in calFolder.get_contents():

		calendar = personalStorage.extract_message(messageInfo).to_mapi_message_item()

		print(calendar.subject)

		calendar.save(dataDir + calendar.subject + "_out.ics")
		
	personalStorage.dispose()
	#ExEnd: SaveCalendarItems
	
if __name__ == '__main__':
    run()
