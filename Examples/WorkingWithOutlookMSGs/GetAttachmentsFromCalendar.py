from aspose.email.mapi import MapiCalendar
from aspose.email.mapi import MapiRecipientType
from aspose.email.mapi import MapiRecipientCollection
from aspose.email.mapi import MapiRecipient
from aspose.email.calendar import AppointmentSaveFormat, Appointment
from aspose.email import MailAddressCollection, Attachment

import datetime as dt
from datetime import timedelta

import os

def run():
	dataDir = "Data/"
	#ExStart: GetAttachmentsFromCalendar
	# Create the appointment
	attendees = MailAddressCollection()
	attendees.append("attendee@domain.com")
	app = Appointment("Room 112", dt.datetime(2018, 5, 27, 22, 12, 11), dt.date(2018, 5, 28), "from@domain.com", attendees)
	app.summary = "Release Meetting";
	app.description = "Discuss for the next release"

	app.attachments.append(Attachment("1.jpg"))
	app.attachments.append(Attachment("1.doc"))

	app.save(dataDir + "appWithAttachments_out.ics", AppointmentSaveFormat.ICS)

	#Read the attachments from CIS
	app2 = Appointment.load(dataDir + "appWithAttachments_out.ics")
	print("Total attachments: " + str(len(app2.attachments)))
	for att in app2.attachments:
		print(att.name)
	#ExEnd: GetAttachmentsFromCalendar
	
if __name__ == '__main__':
    run()
