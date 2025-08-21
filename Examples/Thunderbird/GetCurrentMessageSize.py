import aspose.email
from aspose.email import MailMessage
from aspose.email.storage.mbox import MboxrdStorageReader
from aspose.email.storage.mbox import MboxLoadOptions
import os.path

def run():
	dataDir = "Data/"
        
        #ExStart: GetCurrentMessageSize
	reader = MboxrdStorageReader(dataDir + "ExampleMbox.mbox", MboxLoadOptions())

	eml = reader.read_next_message()

	# Read all messages in a loop
	while (eml is not None):

		print(reader.current_data_size)

		eml.dispose();

		eml = None

	# Close the streams
	reader.dispose();
#ExEnd: GetCurrentMessageSize

if __name__ == '__main__':
    run()
