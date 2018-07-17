from aspose.email import MailMessage, EmlLoadOptions
from aspose.email.storage.pst import *
from aspose.email.mime import HeaderCollection
import aspose.email.mapi.msg as msg
from aspose.email.mapi import MapiMessage, MapiProperty, MapiConversionOptions

def run():
	dataDir = "Data/"
	#ExStart: PreservingEmbeddedMsgFormat
	eml =  MailMessage.load(dataDir + "sample.eml", EmlLoadOptions())

	options = MapiConversionOptions.unicode_format

	options.preserve_embedded_message_format = True

	# Create an instance of the MapiMessage class and pass MailMessage as argument
	outlookMsg = MapiMessage.from_mail_message(eml, options)
	#ExEnd: PreservingEmbeddedMsgFormat
	
if __name__ == '__main__':
    run()
