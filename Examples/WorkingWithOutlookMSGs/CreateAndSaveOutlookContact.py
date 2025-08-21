from aspose.email import MailMessage
from aspose.email.storage.pst import *
from aspose.email.mime import HeaderCollection
import aspose.email.mapi.msg as msg
from aspose.email.mapi import MapiMessage, MapiProperty, ContactSaveFormat
from aspose.email.mapi import MapiContact, MapiContactNamePropertySet, MapiContactProfessionalPropertySet, MapiContactElectronicAddress
from aspose.email.mapi import MapiContactTelephonePropertySet

def run():

	dataDir = "Data/"
	#ExStart: CreateAndSaveOutlookContact
	contact = MapiContact()
	contact.name_info = MapiContactNamePropertySet("Bertha", "A.", "Buell")
	contact.professional_info = MapiContactProfessionalPropertySet("Awthentikz", "Social work assistant")
	contact.personal_info.personal_home_page = "B2BTies.com"
	contact.physical_addresses.work_address.address = "Im Astenfeld 59 8580 EDELSCHROTT"
	contact.electronic_addresses.email1 = MapiContactElectronicAddress("Experwas", "SMTP", "BerthaABuell@armyspy.com")
	contact.telephones = MapiContactTelephonePropertySet("06605045265")
	contact.mileage = "Some test mileage"
	contact.billing = "Test billing information"
	contact.other_fields.journal = True
	contact.personal_info.children = []
	contact.personal_info.children.append("child1")
	contact.personal_info.children.append("child2")
	contact.personal_info.children.append("child3")
	contact.categories = ["category1", "category2", "category3"]

	contact.other_fields.private = True
	##contact.OtherFields.ReminderTime = new DateTime(2014, 1, 1, 0, 0, 55);
	contact.other_fields.reminder_topic = "Test topic"
	contact.other_fields.user_field_1 = "ContactUserField1"
	contact.other_fields.user_field_2 = "ContactUserField2"
	contact.other_fields.user_field_3 = "ContactUserField3"
	contact.other_fields.user_field_4 = "ContactUserField4"

	#Save the Contact in MSG format
	contact.save(dataDir + "CreateAndSaveOutlookContact_out.msg",ContactSaveFormat.MSG)
	#ExEnd: CreateAndSaveOutlookContact
	
if __name__ == '__main__':
    run()
