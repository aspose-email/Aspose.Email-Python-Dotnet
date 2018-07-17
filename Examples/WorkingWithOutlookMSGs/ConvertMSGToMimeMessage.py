from aspose.email import MailMessage
from aspose.email.storage.pst import *
from aspose.email.mime import HeaderCollection
import aspose.email.mapi.msg as msg
from aspose.email.mapi import MapiMessage, MapiProperty, MapiMessageFlags,  MailConversionOptions

def run():
	dataDir = "Data/"
	#ExStart: ConvertMSGToMimeMessage
	# Create an instance of the MapiMessage class
	msg = MapiMessage("sender@test.com","recipient1@test.com; recipient2@test.com","Test Subject","This is a body of message.")
	options = MailConversionOptions()
	options.convert_as_tnef = True
	mail = msg.to_mail_message(options)
	#ExEnd: ConvertMSGToMimeMessage
	
if __name__ == '__main__':
    run()
