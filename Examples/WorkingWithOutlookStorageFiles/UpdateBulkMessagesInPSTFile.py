from aspose.email.storage.pst import *
from aspose.email.mapi import *

def long_to_mapi_bytes(x):
    return x.to_bytes(8, 'little')

def run():
	dataDir = "Data/"
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
	subject  = "New Subject" 
	updatedProperties.add(MapiPropertyTag.SUBJECT_W, MapiProperty(MapiPropertyTag.SUBJECT_W, subject.encode("utf-16")));
	updatedProperties.add(MapiPropertyTag.IMPORTANCE, MapiProperty(MapiPropertyTag.IMPORTANCE, long_to_mapi_bytes(2)));

	# update messages having From = "someuser@domain.com" with new properties
      
	folder.change_messages(changeList, updatedProperties);
	#ExEnd: UpdateBulkMessagesInPSTFile
	
if __name__ == '__main__':
    run()
