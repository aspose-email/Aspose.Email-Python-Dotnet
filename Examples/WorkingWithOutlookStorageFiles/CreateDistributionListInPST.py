from aspose.email.storage.pst import *
from aspose.email.mapi import MapiContact
from aspose.email.mapi import MapiContactNamePropertySet
from aspose.email.mapi import MapiContactElectronicAddress
from aspose.email.mapi import MapiContactGender
from aspose.email.mapi import MapiContactProfessionalPropertySet
from aspose.email.mapi import MapiContactTelephonePropertySet
from aspose.email.mapi import MapiDistributionListMember, MapiDistributionList
from aspose.email.mapi import MapiDistributionListEntryIdType, MapiDistributionListMemberCollection
import base64
import os

def run():
        dataDir = "Data/"

        #ExStart: CreateDistributionListInPST
        displayName1 = "Sebastian Wright"
        email1 = "SebastianWright@dayrep.com"

        displayName2 = "Wichert Kroos"
        email2 = "WichertKroos@teleworm.us"

        os.remove(dataDir + "CreateDistributionListInPST_out.pst")
        personalStorage = PersonalStorage.create(dataDir + "CreateDistributionListInPST_out.pst", FileFormatVersion.UNICODE)

        contactFolder = personalStorage.create_predefined_folder("Contacts", StandardIpmFolder.CONTACTS)

        # Create contacts
        strEntryId1 = contactFolder.add_mapi_message_item(MapiContact(displayName1, email1))
        strEntryId2 = contactFolder.add_mapi_message_item( MapiContact(displayName2, email2))

        member1 = MapiDistributionListMember(displayName1, email1)
        member1.entry_id_type = MapiDistributionListEntryIdType.CONTACT
        member1.entry_id = base64.b64decode( bytes(strEntryId1, "utf-8") )

        member2 = MapiDistributionListMember(displayName2, email2)
        member2.entry_id_type = MapiDistributionListEntryIdType.CONTACT
        member2.entry_id = base64.b64decode( bytes(strEntryId1, "utf-8") )

        members = MapiDistributionListMemberCollection()
        members.append(member1)
        members.append(member2)

        distribution_list = MapiDistributionList("Contact list", members)
        distribution_list.body = "Distribution List Body"
        distribution_list.subject = "Sample Distribution List using Aspose.Email"     
             
        # Add distribution list to PST 
        contactFolder.add_mapi_message_item(distribution_list);
	#ExEnd: CreateDistributionListInPST
	
if __name__ == '__main__':
    run()
