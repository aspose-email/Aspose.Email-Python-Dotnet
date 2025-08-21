from aspose.email import MailMessage
from aspose.email.storage.pst import *
from aspose.email.mime import HeaderCollection
import aspose.email.mapi.msg as msg
from aspose.email.mapi import MapiMessage, MapiProperty, MapiPropertyTag

def run():

	dataDir = "Data/"
	#ExStart: GetMapiProperty
	# Load from file
	msg = MapiMessage.load(dataDir + "message.msg")

	# Access the MapiPropertyTag.PR_SUBJECT property
	prop = msg.properties[MapiPropertyTag.SUBJECT]

	# If the property is not found, check the MapiPropertyTag.PR_SUBJECT_W (which is a // Unicode peer of the MapiPropertyTag.PR_SUBJECT)
	if prop is None:
		prop = msg.properties[MapiPropertyTag.SUBJECT_W]

	# Cannot found
	if prop is None:
		print("No property found!")

	# Get the property data as string
	subject = prop.get_string()

	print("Subject:" + subject)
	# Read internet code page property
	prop = msg.properties[MapiPropertyTag.INTERNET_CPID]
	if prop is not None:
		print("CodePage:" + str(prop.get_long()))
	#ExEnd: GetMapiProperty
	
if __name__ == '__main__':
    run()
