from aspose.email.storage.pst import *

def run():
	dataDir = ""
	#ExStart: SearchingStringInPSTWithIgnoreCaseParameter
	pst = PersonalStorage.from_file(dataDir + "Outlook.pst")
				
	# Get the format of the file
	folder = pst.root_folder.get_sub_folder("Inbox")

	print("Total messges count in folder: " + str(len(folder.get_contents())))

	# Create instance of PersonalStorageQueryBuilder
	queryBuilder = PersonalStorageQueryBuilder()

	queryBuilder.from_address.contains("saqib")
	messages = folder.get_contents(queryBuilder.get_query());
	print("No. of Messages without Ignore Case specified: " + str(len(messages)))

	queryBuilder = PersonalStorageQueryBuilder()
	queryBuilder.from_address.contains("saqib", True)
	messages = folder.get_contents(queryBuilder.get_query())
	print("No. of Messages with Ignore Case specified: " + str(len(messages)))
	#ExEnd: SearchingStringInPSTWithIgnoreCaseParameter

if __name__ == '__main__':
    run()