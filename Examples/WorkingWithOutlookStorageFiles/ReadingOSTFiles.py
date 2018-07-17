from aspose.email.storage.pst import *

def run():
	dataDir = "Data/"
	#ExStart: ReadingOSTFiles
	pst = PersonalStorage.from_file(dataDir + "PersonalStorageFile.ost")
				
	# Get the format of the file
	print("File Format of OST: " + str(pst.format))
	#ExEnd: ReadingOSTFiles
	
if __name__ == '__main__':
    run()
