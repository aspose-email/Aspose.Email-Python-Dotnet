from aspose.email.storage.pst import *

def run():
	dataDir = "Data/"
	#ExStart: DeleteMessagesFromPSTFile
	pst = PersonalStorage.from_file(dataDir + "Outlook.pst")
				
	# Get the format of the file
	folder = pst.get_predefined_folder(StandardIpmFolder.SENT_ITEMS)

	print("Total messges count in folder: " + str(len(folder.get_contents())))

	#Delete First Item
	msgsColl = folder.get_contents()
	msgInfo = msgsColl[0]

	folder.delete_child_item(msgInfo.entry_id)

	print("Total messges count in folder after deletion: " + str(len(folder.get_contents())))
	#ExEnd: DeleteMessagesFromPSTFile
	
if __name__ == '__main__':
    run()
