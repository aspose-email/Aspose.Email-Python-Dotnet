import aspose.email.mapi.msg as msg
from aspose.email.mapi import MapiNote, NoteSaveFormat, NoteColor

def run():

	dataDir = "Data/"
	#ExStart: CreateAndSaveOutlookNote
	note3 = MapiNote()
	note3.subject = "Blue color note"
	note3.body = "This is a blue color note";
	note3.color = NoteColor.YELLOW
	note3.height = 500
	note3.width = 500
	note3.save(dataDir + "CreateAndSaveOutlookNote_out.msg", NoteSaveFormat.MSG)
	#ExEnd: CreateAndSaveOutlookNote
	
if __name__ == '__main__':
    run()
