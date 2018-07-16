from aspose.email import MailMessage
from aspose.email.storage.pst import *
from aspose.email.mime import HeaderCollection
import aspose.email.mapi.msg as msg
from aspose.email.mapi import MapiMessage, FollowUpManager

def run():
	dataDir = ""
	#ExStart: AddingVotingButtonToExistingMessage
	message = MapiMessage.from_file("message.msg")

	FollowUpManager.add_voting_button(message, "Indeed!")

	message.save(dataDir + "AddVotingButtonToExistingMessage_out.msg")
	#ExEnd: AddingVotingButtonToExistingMessage
	
if __name__ == '__main__':
    run()