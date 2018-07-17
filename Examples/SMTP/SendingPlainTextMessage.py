import aspose.email as ae
from aspose.email.clients.smtp import SmtpClient
from aspose.email.clients import SecurityOptions
from aspose.email import MailMessage

def run():
    #ExStart: SendingPlainTextMessage
    eml = ae.MailMessage()
    eml.subject = "Message with Plain Text Body"
    eml.body = "This is plain text body."
    eml.from_address = "from@gmail.com"
    eml.to.append(ae.MailAddress("to@gmail.com", "Recipient 1"))

    #Send using Smtp Client
    client = SmtpClient("smtp.gmail.com", 995, "username", "password")
    client.security_options = SecurityOptions.AUTO

    client.send(eml)
    #ExEnd: SendingPlainTextMessage

if __name__ == '__main__':
    run()
