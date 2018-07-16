from aspose.email.storage.pst import *
from aspose.email.mapi import MapiContact
from aspose.email.mapi import MapiContactNamePropertySet
from aspose.email.mapi import MapiContactElectronicAddress
from aspose.email.mapi import MapiContactGender
from aspose.email.mapi import MapiContactProfessionalPropertySet
from aspose.email.mapi import MapiContactTelephonePropertySet

def run():
	dataDir = ""
	#ExStart: CreateNewMapiContactsAndAddToContactsSubFolder
	# Create three Contacts 
	contact1 =  MapiContact("Sebastian Wright", "SebastianWright@dayrep.com")
	contact2 =  MapiContact("Wichert Kroos", "WichertKroos@teleworm.us", "Grade A Investment")
	contact3 =  MapiContact("Christoffer van de Meeberg", "ChristoffervandeMeeberg@teleworm.us", "Krauses Sofa Factory", "046-630-4614046-630-4614")

	# Contact 4
	contact4 = MapiContact()
	contact4.name_info = MapiContactNamePropertySet("Margaret", "J.", "Tolle")
	contact4.personal_info.gender = MapiContactGender.FEMALE
	contact4.professional_info = MapiContactProfessionalPropertySet("Adaptaz", "Recording engineer")
	contact4.physical_addresses.work_address.address = "4 Darwinia Loop EIGHTY MILE BEACH WA 6725"
	contact4.electronic_addresses.email_1 = MapiContactElectronicAddress("Hisen1988", "SMTP", "MargaretJTolle@dayrep.com")
	contact4.telephones.business_telephone_number = "(08)9080-1183"
	contact4.telephones.mobile_telephone_number = "(925)599-3355(925)599-3355"

	# Contact #5
	contact5 = MapiContact()
	contact5.name_info =  MapiContactNamePropertySet("Matthew", "R.", "Wilcox");
	contact5.personal_info.gender = MapiContactGender.MALE;
	contact5.professional_info = MapiContactProfessionalPropertySet("Briazz", "Psychiatric aide");
	contact5.physical_addresses.work_address.address = "Horner Strasse 12 4421 SAASS";
	contact5.telephones.business_telephone_number = "0650 675 73 300650 675 73 30";
	contact5.telephones.home_telephone_number = "(661)387-5382(661)387-5382";

	# Contact #6
	contact6 = MapiContact();
	contact6.name_info = MapiContactNamePropertySet("Bertha", "A.", "Buell");
	contact6.professional_info = MapiContactProfessionalPropertySet("Awthentikz", "Social work assistant");
	contact6.personal_info.personal_home_page = "B2BTies.com";
	contact6.physical_addresses.work_address.address = "Im Astenfeld 59 8580 EDELSCHROTT";
	contact6.electronic_addresses.email_1 = MapiContactElectronicAddress("Experwas", "SMTP", "BerthaABuell@armyspy.com");
	contact6.telephones = MapiContactTelephonePropertySet("06605045265");

	personalStorage = PersonalStorage.create(dataDir + "SampleContacts_out.pst", FileFormatVersion.UNICODE)

	contactFolder = personalStorage.create_predefined_folder("Contacts", StandardIpmFolder.CONTACTS)
	contactFolder.add_mapi_message_item(contact1)
	contactFolder.add_mapi_message_item(contact2);
	contactFolder.add_mapi_message_item(contact3);
	contactFolder.add_mapi_message_item(contact4);
	contactFolder.add_mapi_message_item(contact5);
	contactFolder.add_mapi_message_item(contact6);

	personalStorage.dispose()
	#ExEnd: CreateNewMapiContactsAndAddToContactsSubFolder
	
if __name__ == '__main__':
    run()