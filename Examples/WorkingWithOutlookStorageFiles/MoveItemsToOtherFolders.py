from aspose.email.storage.pst import *

def run():

	dataDir = "Data/"
	#ExStart: MoveItemsToOtherFolders
	personalStorage = PersonalStorage.from_file(dataDir + "test.pst")

	# Get the format of the file
	inbox = personalStorage.root_folder.get_sub_folder("Inbox")

	deleted = personalStorage.get_predefined_folder(StandardIpmFolder.DELETED_ITEMS)

	subfolder = inbox.get_sub_folder("SubInbox")

	# Move folder and message to the Deleted Items
	personalStorage.move_item(subfolder, deleted)
	contents = subfolder.get_contents()
	personalStorage.move_item(contents[0], deleted)
		
	# Move all inbox subfolders and subfolder contents to the Deleted Items
	inbox.move_subfolders(deleted)
	subfolder.move_contents(deleted)
	#ExEnd: MoveItemsToOtherFolders
	
if __name__ == '__main__':
    run()
