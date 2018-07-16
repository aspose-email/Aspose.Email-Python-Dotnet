from aspose.email import MailMessage
from aspose.email.storage.pst import *
from aspose.email.mime import HeaderCollection
import aspose.email.mapi.msg as msg
from aspose.email.mapi import MapiMessage, MapiProperty, MapiMessageFlags

def run():
	dataDir = ""
	#ExStart: SavingMessageInDraftStatus
	# Create an instance of the MapiMessage class
	outlookMsg = MapiMessage()

	# Set Message Body
	outlookMsg.body = "Message created with MapiMessage in draft mode."

	#Set the Unsent flag
	outlookMsg.set_message_flags(MapiMessageFlags.UNSENT)

	# Save the message (MSG) file
	strMsgFile = "SavingMessageInDraftStatus_out.msg"
	outlookMsg.save(dataDir + strMsgFile);
	#ExEnd: SavingMessageInDraftStatus
	
if __name__ == '__main__':
    run()