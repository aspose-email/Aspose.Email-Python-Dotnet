from aspose.email.storage.pst import *

def run():
	dataDir = ""
	#ExStart: UpdateBulkMessagesInPSTFile
	pst = PersonalStorage.from_file(dataDir + "test.pst")
				
	# Get the format of the file
	folder = pst.root_folder.get_sub_folder("Inbox")

	print("Total messges count in folder: " + str(len(folder.get_contents())))

	# Create instance of PersonalStorageQueryBuilder
	queryBuilder = PersonalStorageQueryBuilder()
	queryBuilder.from_address.contains("saqib", True)
	messages = folder.get_contents(queryBuilder.get_query())
	print("No. of Messages with specified criterion: " + str(len(messages)))

	changeList = []
	for messageInfo in messages:
		changeList.append(messageInfo.entry_id_string)
		
	# Compose the new properties
	updatedProperties = MapiPropertyCollection()
	updatedProperties.Add(MapiPropertyTag.PR_SUBJECT_W, new MapiProperty(MapiPropertyTag.PR_SUBJECT_W, Encoding.Unicode.GetBytes("New Subject")));
	updatedProperties.Add(MapiPropertyTag.PR_IMPORTANCE, new MapiProperty(MapiPropertyTag.PR_IMPORTANCE, BitConverter.GetBytes((long)2)));

	# update messages having From = "someuser@domain.com" with new properties
	inbox.ChangeMessages(changeList, updatedProperties);
	#ExEnd: UpdateBulkMessagesInPSTFile
	
if __name__ == '__main__':
    run()
