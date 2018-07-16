from aspose.email.storage.pst import *
from aspose.email.mapi import MapiContact
from aspose.email.mapi import ContactSaveFormat

def run():
	dataDir = ""
	#ExStart: AccessContactInformation
	pst = PersonalStorage.from_file(dataDir + "SampleContacts_out.pst")
				
	folderInfo = pst.get_predefined_folder(StandardIpmFolder.CONTACTS)

	messageInfoCollection = folderInfo.get_contents()
	for  messageInfo in messageInfoCollection:

		# Get the contact information
		mapi = pst.extract_message(messageInfo)

		contact = mapi.to_mapi_message_item()

		# Display some contents on screen
		print("Name: " + contact.name_info.display_name)

		#Save to disc in MSG Format
		if contact.name_info.display_name is not None:
			
			contact.save(dataDir + "Contacts\\" + contact.name_info.display_name + "_out.msg")

			contact.save(dataDir + "Contacts\\" + contact.name_info.display_name + "_out.vcf", ContactSaveFormat.VCARD)
	#ExEnd: AccessContactInformation
	
if __name__ == '__main__':
    run()