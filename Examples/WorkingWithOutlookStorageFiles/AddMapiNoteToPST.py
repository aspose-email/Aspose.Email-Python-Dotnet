from aspose.email.storage.pst import *
from aspose.email.mapi import MapiNote
from aspose.email.mapi import NoteColor

import datetime as dt
from datetime import timedelta

def run():
	dataDir = ""
	#ExStart:AddMapiNoteToPST
	# Create three Notes  
	note1 = MapiNote()
	note1.subject = "Yellow color note"
	note1.body = "This is a yellow color note"

	note2 = MapiNote()
	note2.subject = "Pink color note"
	note2.body = "This is a pink color note"
	note2.color = NoteColor.PINK

	note3 = MapiNote()
	note2.subject = "Blue color note";
	note2.body = "This is a blue color note";
	note2.color = NoteColor.BLUE
	note3.height = 500
	note3.width = 500

	personalStorage = PersonalStorage.create(dataDir + "AddMapiNoteToPST_out.pst", FileFormatVersion.UNICODE)

	notesFolder = personalStorage.create_predefined_folder("Tasks", StandardIpmFolder.NOTES)
	notesFolder.add_mapi_message_item(note1)
	notesFolder.add_mapi_message_item(note2)
	notesFolder.add_mapi_message_item(note3)
	personalStorage.dispose()
	#ExEnd: AddMapiNoteToPST
	
if __name__ == '__main__':
    run()