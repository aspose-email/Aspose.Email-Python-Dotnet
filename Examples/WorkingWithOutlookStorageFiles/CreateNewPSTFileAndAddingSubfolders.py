from aspose.email.storage.pst import *
from aspose.email.mapi import MapiMessage

def run():
	dataDir = "Data/"
	#ExStart: CreateNewPSTFileAndAddingSubfolders
	pst = PersonalStorage.create(dataDir + "PstWithPython_out.pst", FileFormatVersion.UNICODE)

	# Add new folder "Inbox"
	pst.root_folder.add_sub_folder("Inbox");

	pst.dispose()
	#ExEnd: CreateNewPSTFileAndAddingSubfolders
	
if __name__ == '__main__':
    run()
