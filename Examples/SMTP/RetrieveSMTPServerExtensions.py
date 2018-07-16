import aspose.email as ae
from aspose.email.clients.smtp import SmtpClient
from aspose.email.clients import SecurityOptions
from aspose.email import MailMessage

#ExStart: RetrieveSMTPServerExtensions

client = SmtpClient("smtp.gmail.com", 587, "kashif.iqbal.aspose", "aspose1234")
client.security_options = SecurityOptions.AUTO
caps = []
caps = client.get_capabilities()

for str in caps:
    print(str)
#ExEnd: RetrieveSMTPServerExtensions
