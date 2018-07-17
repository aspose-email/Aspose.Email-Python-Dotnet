from aspose.email.storage.pst import *

def run():
	dataDir = "Data/"
	#ExStart: ConvertingOSTToPST
	pst = PersonalStorage.from_file(dataDir + "PersonalStorageFile.ost")
				
	# Get the format of the file
	pst.save_as(dataDir + "ConvertOSTToPst_out.pst", FileFormat.PST)
	#ExEnd: ConvertingOSTToPST
	
if __name__ == '__main__':
    run()
