from aspose.email.storage.pst import *
from aspose.email.mime import HeaderCollection
import aspose.email.mapi.msg as msg 
from aspose.email.mapi import MapiMessage

def run():
	dataDir = ""
	#ExStart: DisplayReceipientsStatusFromMeetingReqeust
	message = MapiMessage.from_file("filename.msg")
	for recipient in message.recipients:
		print(recipient.recipient_track_status)
	#ExEnd: DisplayReceipientsStatusFromMeetingReqeust
	
if __name__ == '__main__':
    run()