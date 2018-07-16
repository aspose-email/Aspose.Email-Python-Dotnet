from aspose.email.storage.pst import *

def run():
	dataDir = ""
	#ExStart: AddFilesToPST
	personalStorage = PersonalStorage.create(dataDir + "AddFilesToPst_out.pst", FileFormatVersion.UNICODE)

	folder = personalStorage.root_folder.add_sub_folder("Files")

	folder.add_file(dataDir + "FileToBeAddedToPST.txt", "")
	#ExEnd: AddFilesToPST
	
if __name__ == '__main__':
    run()