import aspose.email as ae
from aspose.email import MailAddress
from aspose.email import MailAddressCollection
from aspose.email.calendar import Appointment
from aspose.email.calendar import AppointmentSaveFormat

import datetime as dt
from datetime import timedelta

def run():
    dataDir = "Data/"
    #ExStart: CreateAppointment
    #Create Appointment instance
    attendees = MailAddressCollection()
    attendees.append(MailAddress("attendee@domain.com"))
    app = Appointment("Room 112", dt.datetime(2018, 5, 27, 22, 12, 11), dt.date(2018, 5, 28), MailAddress("from@domain.com"), attendees);
    app.summary = "Release Meetting";
    app.description = "Discuss for the next release"

    app.save("AppointmentInICSFormat_out.ics", AppointmentSaveFormat.ICS)
    #ExEnd: CreateAppointment

if __name__ == '__main__':
    run()
