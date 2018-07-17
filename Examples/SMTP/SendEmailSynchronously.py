import aspose.email as ae
from aspose.email.clients.smtp import SmtpClient
from aspose.email.clients import SecurityOptions
from aspose.email import MailMessage

def run():
    #ExStart: SendEmailSynchronously
    eml = ae.MailMessage()
    eml.subject = "New MailMessage created with Aspose.Email for Python"
    eml.html_body = "<b>This line is in bold </b> while this is normal text"
    eml.from_address = "from@domain.com"

    eml.to.append(ae.MailAddress("to@domain.com", "Recipient 1"))
    eml.to.append(ae.MailAddress("to2@domain.com", "Recipient 2"))

    eml.cc.append(ae.MailAddress("cc1@domain.com", "Recipient 3"))
    eml.cc.append(ae.MailAddress("cc2@domain.com", "Recipient 4"))

    #Send using Smtp Client
    client = SmtpClient("smtp.gmail.com", 587, "username", "password")
    client.security_options = SecurityOptions.AUTO
    client.send(eml)
    #ExEnd: SendEmailSynchronously
if __name__ == '__main__':
    run()
