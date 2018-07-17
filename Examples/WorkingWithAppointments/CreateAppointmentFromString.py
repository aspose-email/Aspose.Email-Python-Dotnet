import aspose.email as ae
from aspose.email import MailAddressCollection
from aspose.email.calendar import Appointment
from aspose.email.calendar import AppointmentSaveFormat
from aspose.email.calendar import AppointmentMethodType
from aspose.email import MailMessage
from aspose.email.mapi import MapiMessage
from aspose.email.mime import ContentType
from aspose.email import *

import datetime as dt
from datetime import timedelta

def run():
    dataDir = "Data/"
    #ExStart: CreateAppointmentFromString
    ical = """BEGIN:VCALENDAR
    METHOD:PUBLISH
    PRODID:-//Aspose Ltd//iCalender Builder (v3.0)//EN
    VERSION:2.0
    BEGIN:VEVENT
    ATTENDEE;CN=test@gmail.com:mailto:test@gmail.com
    DTSTART:20130220T171439
    DTEND:20130220T174439
    DTSTAMP:20130220T161439Z
    END:VEVENT
    END:VCALENDAR"""

    sender = "test@gmail.com"
    recipient = "test@email.com"
    message =  MailMessage(sender, recipient, "", "")
    av = AlternateView.create_alternate_view_from_string(ical, ContentType("text/calendar"))
    message.alternate_views.append(av)
    msg = MapiMessage.from_mail_message(message)
    msg.save(dataDir + "draft_out.msg")
    #ExEnd: CreateAppointmentFromString

if __name__ == '__main__':
    run()
