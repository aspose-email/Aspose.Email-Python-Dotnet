import aspose.email as ae
from aspose.email import MailAddressCollection
from aspose.email.calendar import Appointment
from aspose.email.calendar import AppointmentSaveFormat
from aspose.email.calendar import AppointmentMethodType
from aspose.email import MailMessage
from aspose.email.mapi import MapiMessage

import datetime as dt
from datetime import timedelta

def run():
    dataDir = "Data/"
    #ExStart: DraftAppointmentRequest
    #Create Appointment instance
    attendees = MailAddressCollection()
    attendees.append("attendee@domain.com")
    app = Appointment("Room 112", dt.datetime(2018, 5, 27, 22, 12, 11), dt.date(2018, 5, 28), "from@domain.com", attendees);
    app.summary = "Release Meetting";
    app.description = "Discuss for the next release"
    app.method_type = AppointmentMethodType.PUBLISH

    message = MailMessage("sender@domain.com", "recipient@domain.com", "", "")

    message.add_alternate_view(app.request_apointment())

    msg = MapiMessage.from_mail_message(message)

    # Save the appointment as draft.
    msg.save(dataDir + "DraftAppointmentRequest_out.msg")
    #ExEnd: DraftAppointmentRequest

if __name__ == '__main__':
    run()
