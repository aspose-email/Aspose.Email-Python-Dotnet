from aspose.email import MailMessage
from aspose.email.mime import HeaderCollection
import aspose.email.mapi.msg as msg
from aspose.email.mapi import MapiMessage, MapiContact
from aspose.email.personalinfo.vcard import VCardContact

def run():
	dataDir = "Data/"
	#ExStart: LoadingContactFromVCF

	vcard_contact = VCardContact.load(dataDir + "Contact.vcf")
	print('Email Address: ', vcard_contact.emails[0].email_address)

	#ExEnd: LoadingContactFromVCF
	
if __name__ == '__main__':
    run()
