import aspose.email
from aspose.email import MailMessage
from aspose.email.storage.mbox import MboxrdStorageReader
from aspose.email.storage.mbox import MboxLoadOptions
import os.path

def run():
	dataDir = "Data/"
        
	reader = MboxrdStorageReader(dataDir + "ExampleMbox.mbox", MboxLoadOptions())

	print(reader.current_data_size)
	eml = reader.read_next_message()

	# Read all messages in a loop
	while (eml is not None):
		print("Subject: " + eml.subject)
		eml = reader.read_next_message()

if __name__ == '__main__':
    run()
