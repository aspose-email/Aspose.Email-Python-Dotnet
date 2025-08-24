from aspose.email import MailMessage
from aspose.email.storage.pst import *
from aspose.email.mime import HeaderCollection
import aspose.email.mapi.msg as msg
from aspose.email.mapi import MapiMessage, FollowUpManager, FollowUpOptions, MapiPropertyTag 

def run():

	dataDir = "Data/"
	#ExStart: ReadVoteResultsInformation
	msg = MapiMessage.load(dataDir + "AddVotingButtonToExistingMessage.msg");
	for recipient in msg.recipients:
		print("Recipient: {0}".format(recipient.display_name))

		#get the PR_RECIPIENT_AUTORESPONSE_PROP_RESPONSE property
		response_prop = recipient.properties[MapiPropertyTag.RECIPIENT_AUTORESPONSE_PROP_RESPONSE]
		if response_prop is not None:
			print(f"Response: {response_prop}")

		#Get the PR_RECIPIENT_TRACKSTATUS_TIME property
		mt = recipient.properties[MapiPropertyTag.RECIPIENT_TRACKSTATUS_TIME]
		if mt is not None:
			mt_value = mt.get_date_time()
			print("Response time: {}".format(mt_value))
	#ExEnd: ReadVoteResultsInformation
	
if __name__ == '__main__':
    run()
