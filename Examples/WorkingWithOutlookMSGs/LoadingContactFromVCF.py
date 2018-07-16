from aspose.email import MailMessage
from aspose.email.mime import HeaderCollection
import aspose.email.mapi.msg as msg
from aspose.email.mapi import MapiMessage, MapiContact
from aspose.email.personalinfo.vcard import VCardContact

def run():
	dataDir = ""
	#ExStart: LoadingContactFromVCF
	VCardContact.load(dataDir + "Contact.vcf")

	apiContact = MapiContact.from_vcard(dataDir + "Contact.vcf")
	#ExEnd: LoadingContactFromVCF
	
if __name__ == '__main__':
    run()