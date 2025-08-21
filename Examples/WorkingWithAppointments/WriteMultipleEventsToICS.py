import aspose.email as ae
from aspose.email import MailAddress
from aspose.email import MailAddressCollection
from aspose.email.calendar import CalendarWriter
from aspose.email.calendar import AppointmentIcsSaveOptions
from aspose.email.calendar import AppointmentAction
from aspose.email.calendar import Appointment

import datetime as dt
from datetime import timedelta

def run():
    dataDir = "Data/"
    #ExStart: WriteMultipleEventsToICS
    saveOptions = AppointmentIcsSaveOptions()
    saveOptions.action = AppointmentAction.CREATE

    writer = CalendarWriter(dataDir + "WriteMultipleEventsToICS_out.ics", saveOptions)

    attendees = MailAddressCollection()
    attendees.append("attendee@domain.com")

    for i in range(10):
        app = Appointment("Room 112", dt.datetime(2018, 5, 27, 22, 12, 11), dt.date(2018, 5, 28), MailAddress("from@domain.com"), attendees)
        app.description = "Test body " + str(i)
        app.summary = "Test summary:" + str(i)
        writer.write(app)  
    #ExEnd: WriteMultipleEventsToICS

if __name__ == '__main__':
    run()
