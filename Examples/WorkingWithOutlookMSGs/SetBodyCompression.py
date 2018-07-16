from aspose.email import MailMessage
import aspose.email.mapi.msg as msg
from aspose.email.mapi import MapiMessage, MapiConversionOptions

def run():
	#ExStart: SetBodyCompression
	eml = MailMessage.load("CreatingAndSavingOutlookMessages_out.msg");
	options = MapiConversionOptions()
	options.use_body_compression = True
	ae_mapi = MapiMessage.from_mail_message(eml, options);
	#ExEnd: SetBodyCompression
	
if __name__ == '__main__':
    run()