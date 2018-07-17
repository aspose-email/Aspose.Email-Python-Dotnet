from aspose.email import MailMessage
from aspose.email.storage.pst import *
from aspose.email.mime import HeaderCollection
import aspose.email.mapi.msg as msg
from aspose.email.mapi import MapiMessage, MapiProperty

def run():
	dataDir = "Data/"
	
	#ExStart: CreatingMSGFilesWithRtfBody
	eml = MailMessage()
	eml.is_draft = True

	# Create an instance of the MapiMessage class and pass MailMessage as argument
	outlookMsg = MapiMessage.from_mail_message(eml)

	# Set RTF Body
	outlookMsg.body_rtf = "{\\rtf1\\ansi\\ansicpg1252\\deff0\\deflang1033{\\fonttbl{\\f0\\fnil\\fcharset0 Calibri;}}\r\n{\\*\\generator Msftedit 5.41.21.2510;}\\viewkind4\\uc1\\pard\\sa200\\sl276\\slmult1\\lang9\\f0\\fs22 This is RTF Body with this \\b bold \\b0 text.\\par\r\n}\r\n\0"
				
	# Save the message (MSG) file
	strMsgFile = "CreatingMSGFilesWithRtfBody_out.msg"
	outlookMsg.save(dataDir + strMsgFile);
	#ExEnd: CreatingMSGFilesWithRtfBody
	
if __name__ == '__main__':
    run()
