from aspose.email import MailMessage
from aspose.email.mime import HeaderCollection
import aspose.email.mapi.msg as msg
from aspose.email.mapi import MapiMessage, MapiContact
from aspose.email.personalinfo.vcard import VCardContact

def run():

	dataDir = "Data/"
	#ExStart: LoadingContactFromVCardWithSpecifiedEncoding
	contactReadFromFile = MapiContact.from_vcard(dataDir + "Contact.vcf", "UTF-8")
	#ExEnd: LoadingContactFromVCardWithSpecifiedEncoding
	
if __name__ == '__main__':
    run()
