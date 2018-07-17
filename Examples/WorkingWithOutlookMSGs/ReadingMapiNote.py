from aspose.email.mapi import MapiMessage
from aspose.email.mapi import MapiNote, NoteSaveFormat, NoteColor

def run():
	dataDir = "Data/"
	#ExStart: ReadingMapiNote
	note = MapiMessage.from_file(dataDir + "CreateAndSaveOutlookNote_out.msg")
	note2 = note.to_mapi_message_item()
	#ExEnd: ReadingMapiNote
	
if __name__ == '__main__':
    run()
