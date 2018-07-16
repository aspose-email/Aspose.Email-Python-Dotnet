from aspose.email.mapi import MapiCalendar
from aspose.email.mapi import MapiRecipientType
from aspose.email.mapi import MapiRecipientCollection
from aspose.email.mapi import MapiRecipient
from aspose.email.calendar import AppointmentSaveFormat

import datetime as dt
from datetime import timedelta

import os

def run():
	dataDir = ""
	#ExStart: AddDisplayReminderToCalendar
	# Create the appointment
	calendar = MapiCalendar(
		"LAKE ARGYLE WA 6743",
		"Appointment",
		"This is a very important meeting :)",
		dt.datetime(2018, 6, 1, 21, 30, 0),
		dt.datetime(2018, 6, 1, 21, 50, 0))

	calendar.reminder_set= True
	calendar.reminder_delta = 45 #45 min before start of event

	calendar.save(dataDir + "AddDisplayReminderToCalendar_out.ics", AppointmentSaveFormat.ICS)

	calendar.save(dataDir + "AddDisplayReminderToCalendar_out.Msg", AppointmentSaveFormat.MSG)
	#ExEnd: AddDisplayReminderToCalendar
	
if __name__ == '__main__':
    run()
	