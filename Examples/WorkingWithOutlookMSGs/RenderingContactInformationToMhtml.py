from aspose.email import MailMessage, MhtFormatOptions, MhtSaveOptions, ContactFieldsSet
from aspose.email.mime import HeaderCollection
import aspose.email.mapi.msg as msg
from aspose.email.mapi import MapiMessage, MapiContact, MailConversionOptions
from aspose.email.personalinfo.vcard import VCardContact

def run():

	dataDir = "Data/"
	#ExStart: RenderingContactInformationToMhtml
	msg = MapiMessage.load(dataDir + "Contact.msg")
	op = MailConversionOptions()
	eml = msg.to_mail_message(op)

	#Prepare the MHT format options
	mhtSaveOptions = MhtSaveOptions()
	mhtSaveOptions.check_body_content_encoding = True
	mhtSaveOptions.preserve_original_boundaries = True
	formatOp = MhtFormatOptions.WRITE_HEADER | MhtFormatOptions.RENDER_VCARD_INFO
	mhtSaveOptions.rendered_contact_fields = ContactFieldsSet.NAME_INFO | ContactFieldsSet.PERSONAL_INFO | ContactFieldsSet.TELEPHONES | ContactFieldsSet.EVENTS
	mhtSaveOptions.mht_format_options = formatOp
	eml.save(dataDir + "RenderingContactInformationToMhtml_out.mhtml", mhtSaveOptions)
	#ExEnd: RenderingContactInformationToMhtml
	
if __name__ == '__main__':
    run()
