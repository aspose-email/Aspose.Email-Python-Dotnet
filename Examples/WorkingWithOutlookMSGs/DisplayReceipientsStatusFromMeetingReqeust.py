from aspose.email.storage.pst import *
from aspose.email.mime import HeaderCollection
import aspose.email.mapi.msg as msg 
from aspose.email.mapi import MapiMessage

def run():
	dataDir = "Data/"
	#ExStart: DisplayReceipientsStatusFromMeetingReqeust
	message = MapiMessage.load(dataDir + "filename.msg")
	for recipient in message.recipients:
		print(recipient.recipient_track_status)
	#ExEnd: DisplayReceipientsStatusFromMeetingReqeust
	
if __name__ == '__main__':
    run()
