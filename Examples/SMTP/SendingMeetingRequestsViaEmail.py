import aspose.email as ae
from aspose.email.clients.smtp import SmtpClient
from aspose.email.clients import SecurityOptions
from aspose.email import MailMessage
from aspose.email.calendar import Appointment

import datetime as dt
from datetime import timedelta

#ExStart: SendingMeetingRequestsViaEmail
eml = ae.MailMessage()
eml.from_address = "from@gmail.com"
eml.to.append(ae.MailAddress("to@gmail.com", "Recipient 1"))

#Create Appointment instance
app = Appointment("Room 112", dt.datetime(2018, 5, 27, 22, 12, 11), dt.date(2018, 5, 28), eml.from_address, eml.to);
app.summary = "Release Meetting";
app.description = "Discuss for the next release"

eml.add_alternate_view(app.request_apointment())

#Send using Smtp Client
client = SmtpClient("smtp.gmail.com", 995, "username", "password")
client.security_options = SecurityOptions.AUTO

client.send(eml)
#ExEnd: SendingMeetingRequestsViaEmail
