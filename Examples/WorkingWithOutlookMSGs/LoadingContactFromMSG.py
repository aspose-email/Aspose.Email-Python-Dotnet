from aspose.email import MailMessage
from aspose.email.storage.pst import *
from aspose.email.mime import HeaderCollection
import aspose.email.mapi.msg as msg
from aspose.email.mapi import MapiMessage, MapiProperty, FollowUpManager

def run():
	dataDir = ""
	#ExStart: LoadingContactFromMSG
	message = MapiMessage.from_file("Contact.msg")

	apiContact = message.to_mapi_message_item()
	#ExEnd: LoadingContactFromMSG
	
if __name__ == '__main__':
    run()