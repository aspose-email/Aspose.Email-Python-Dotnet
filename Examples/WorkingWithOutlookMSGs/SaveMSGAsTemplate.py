from aspose.email import MailMessage
from aspose.email.storage.pst import *
from aspose.email.mime import HeaderCollection
import aspose.email.mapi.msg as msg
from aspose.email.mapi import MapiMessage, MapiProperty, MapiMessageFlags,  MailConversionOptions

def run():
	dataDir = ""
	#ExStart: SaveMSGAsTemplate
	# Create an instance of the MapiMessage class
	msg = MapiMessage("sender@test.com","recipient1@test.com; recipient2@test.com","Test Subject","This is a body of message.")

	msg.save_as_template("SaveMsgAsTemplate_out.msg");
	#ExEnd: SaveMSGAsTemplate
	
if __name__ == '__main__':
    run()