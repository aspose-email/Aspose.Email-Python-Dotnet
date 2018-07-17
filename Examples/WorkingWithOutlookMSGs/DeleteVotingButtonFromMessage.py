from aspose.email import MailMessage
from aspose.email.storage.pst import *
from aspose.email.mime import HeaderCollection
import aspose.email.mapi.msg as msg
from aspose.email.mapi import MapiMessage, FollowUpManager, FollowUpOptions

def run():
	dataDir = "Data/"
	#ExStart: DeleteVotingButtonFromMessage
	message = MapiMessage.from_file("message.msg")

	FollowUpManager.add_voting_button(message, "Indeed!")

	message.save(dataDir + "AddVotingButtonToExistingMessage_out.msg")

	eml = MailMessage("from@gmail.com", "to@gmail.com", "Subject", "Body")
	eml.is_draft = False
	msg = MapiMessage.from_mail_message(eml)

	options = FollowUpOptions()
	options.voting_buttons = "Yes;No;Maybe;Exactly!"
	FollowUpManager.set_options(msg, options)
	msg.save(dataDir + "MapiMsgWithPoll.msg")
	FollowUpManager.remove_voting_button(msg, "Exactly!");#Deleting a single button OR
	FollowUpManager.clear_voting_buttons(msg) # Deleting all buttons from a MapiMessage
	msg.save(dataDir + "MapiMsgWithPoll_out.msg")
	#ExEnd: DeleteVotingButtonFromMessage
	
if __name__ == '__main__':
    run()
