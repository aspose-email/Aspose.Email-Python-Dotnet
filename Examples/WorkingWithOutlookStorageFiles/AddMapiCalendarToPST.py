from aspose.email.storage.pst import *
from aspose.email.mapi import MapiCalendar
from aspose.email.mapi import MapiRecipientType
from aspose.email.mapi import MapiRecipientCollection
from aspose.email.mapi import MapiRecipient

import datetime as dt
from datetime import timedelta

import os

def run():
	dataDir = "Data/"
	#ExStart: AddMapiCalendarToPST
	# Create the appointment
	appointment = MapiCalendar(
		"LAKE ARGYLE WA 6743",
		"Appointment",
		"This is a very important meeting :)",
		dt.datetime(2018, 6, 1, 21, 30, 0),
		dt.datetime(2018, 6, 1, 21, 50, 0))

	# Create the meeting
	attendees = MapiRecipientCollection()
	attendees.add("ReneeAJones@armyspy.com", "Renee A. Jones", MapiRecipientType.TO)
	attendees.add("SzllsyLiza@dayrep.com", "Szollosy Liza", MapiRecipientType.TO)

	meeting =  MapiCalendar(
		"Meeting Room 3 at Office Headquarters",
		"Meeting",
		"Please confirm your availability.",
		dt.datetime(2018, 6, 1, 21, 30, 0),
		dt.datetime(2018, 6, 1, 21, 50, 0),
		"CharlieKhan@dayrep.com",
		attendees
		)

	os.remove(dataDir + "AddMapiCalendarToPST_out.pst")
	personalStorage = PersonalStorage.create(dataDir + "AddMapiCalendarToPST_out.pst", FileFormatVersion.UNICODE)

	calFolder = personalStorage.create_predefined_folder("AsposeCalendar", StandardIpmFolder.APPOINTMENTS)
	calFolder.add_mapi_message_item(appointment)
	calFolder.add_mapi_message_item(meeting)

	personalStorage.dispose()
	#ExEnd: AddMapiCalendarToPST
