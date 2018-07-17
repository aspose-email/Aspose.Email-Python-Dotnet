from aspose.email.mapi import MapiMessage, MapiProperty

def run():
	dataDir = "Data/"
	#ExStart: LoadMsgFiles
	# Create an instance of MapiMessage from file
	msg = MapiMessage.from_file(dataDir + "CreatingAndSavingOutlookMessages_out.msg")

	# Get subject
	print("Subject: " + msg.subject)

	# Get from address
	print("From: " + msg.sender_email_address)

	# Get body
	print("Body: " + msg.body)

	# Get recipients information
	print("Recipients Count: " + str(len(msg.recipients)))

	# Get Attachments information
	print ("Attachments Count:" + str(len(msg.attachments)))

	# Print attachments information
	for index, att in enumerate(msg.attachments):
		if att.object_data is not None:
			print(att.display_name)
	#ExEnd: LoadMsgFiles
	
if __name__ == '__main__':
    run()
