from aspose.email import MailMessage
from aspose.email.storage.pst import *
from aspose.email.mime import HeaderCollection
import aspose.email.mapi.msg as msg
from aspose.email.mapi import MapiMessage, FollowUpManager

def run():
	dataDir = ""
	#ExStart: ReadingOnlyVotingButtons
	message = MapiMessage.from_file("MessageWithVotingResponded.msg")

	buttons = FollowUpManager.get_voting_buttons(message)

	for button in buttons:
		print(button)
	#ExEnd: ReadingOnlyVotingButtons
	
if __name__ == '__main__':
    run()