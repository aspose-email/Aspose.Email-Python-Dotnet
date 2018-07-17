from aspose.email import MailMessage
from aspose.email.storage.pst import *
from aspose.email.mime import HeaderCollection
import aspose.email.mapi.msg as msg
from aspose.email.mapi import MapiMessage, MapiProperty
from aspose.email import Attachment

def run():
	dataDir = "Data/"
	#ExStart: AddingMSGAttachments
	eml =  MailMessage()

	# Set from, to, subject and body properties
	eml.from_address = "sender@domain.com";
	eml.to.append("receiver@domain.com");
	eml.subject = "This is test message";
	eml.body = "This is test body";

	#Add attachments to MailMessage
	eml.add_attachment(Attachment(dataDir + "1.jpg"))
	eml.add_attachment(Attachment(dataDir + "1.doc"))
	eml.add_attachment(Attachment(dataDir + "1.pdf"))

	# Create an instance of the MapiMessage class and pass MailMessage as argument
	outlookMsg = MapiMessage.from_mail_message(eml);
				
	# Save the message (MSG) file
	strMsgFile = "AddingMSGAttachments_out.msg"
	outlookMsg.save(dataDir + strMsgFile);
	#ExEnd: AddingMSGAttachments
	
if __name__ == '__main__':
    run()
