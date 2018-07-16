from aspose.email.storage.pst import *

define run():
	dataDir = ""
	#ExStart: DeleteBulkItemsFromPst
	pst = PersonalStorage.from_file(dataDir + "Outlook.pst")
				
	# Get the format of the file
	folder = pst.get_predefined_folder(StandardIpmFolder.INBOX)

	print("Total messges count in folder: " + str(len(folder.get_contents())))

	# Create instance of PersonalStorageQueryBuilder
	queryBuilder = PersonalStorageQueryBuilder()

	queryBuilder.subject.contains("Microsoft")
	messages = folder.get_contents(queryBuilder.get_query());

	print("No. of Messages as per specified criterion: " + str(len(messages)))
	deleteList = []

	for messageInfo in messages:
		deleteList.append(messageInfo.entry_id_string)

	folder.delete_child_items(deleteList)
	#ExEnd: DeleteBulkItemsFromPst
	
if __name__ == '__main__':
    run()