from aspose.email import MailMessage
from aspose.email.storage.pst import *
from aspose.email.mime import HeaderCollection
import aspose.email.mapi.msg as msg
from aspose.email.mapi import MapiMessage, MapiProperty, FollowUpManager

def run():

	dataDir = "Data/"
	#ExStart: ReadingVotingOptions
	message = MapiMessage.load(dataDir + "MessageWithVotingResponded.msg")

	# This method can be useful when except voting buttons it is necessary to get other parameters (ex. a category)
	options = FollowUpManager.get_options(message)

	# Voting buttons will be introduced as a string with semi-column as a separator
	votingButtons = options.voting_buttons

	print(votingButtons)
	#ExEnd: ReadingVotingOptions
	
if __name__ == '__main__':
    run()
