import aspose.email as ae
from aspose.email import MailAddressCollection
from aspose.email.calendar import CalendarReader

import datetime as dt
from datetime import timedelta

def run():
    dataDir = ""

    #ExStart: ReadMultipleEventsFromICS
    #Load Appointment instance
    reader = CalendarReader(dataDir + "US-Holidays.ics")

    appointments = []

    while reader.next_event():
        appointments.append(reader.current)

    print ("Total Appointments: " + str(len(appointments)))
    #ExEnd: ReadMultipleEventsFromICS

if __name__ == '__main__':
    run()
