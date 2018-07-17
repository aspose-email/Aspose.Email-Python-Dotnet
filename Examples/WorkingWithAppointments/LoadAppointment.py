import aspose.email as ae
from aspose.email import MailAddressCollection
from aspose.email.calendar import Appointment
from aspose.email.calendar import AppointmentSaveFormat

import datetime as dt
from datetime import timedelta

def run():
    dataDir = "Data/"
    #ExStart: LoadAppointment
    #Load Appointment instance
    loadedAppointment = Appointment.load(dataDir + "AppointmentInICSFormat_out.ics")
    print("Summary: " + loadedAppointment.summary)
    print("Location: " + loadedAppointment.location)
    print("Description: " + loadedAppointment.description)
    print("Start date: " + str(loadedAppointment.start_date))
    print("End date: " + str(loadedAppointment.end_date))
    print("Organizer: " + loadedAppointment.organizer.address)
    print("Attendees: " + loadedAppointment.attendees[0].address)
    #ExEnd: LoadAppointment

if __name__ == '__main__':
    run()
