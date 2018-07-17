import aspose.email as ae
from aspose.email.clients.smtp import SmtpClient
from aspose.email.clients import SecurityOptions
from aspose.email import MailMessage

def run():
    #ExStart: SendMsgAsTNEF
    eml = MailMessage.load("Message.eml")
    eml.subject = "Send message as TNEF"
    eml.from_address = "from@gmail.com"
    eml.to.append(ae.MailAddress("to@gmail.com", "Recipient 1"))

    #Send using Smtp Client
    client = SmtpClient("smtp.gmail.com", 995, "username", "password")
    client.security_options = SecurityOptions.AUTO
    client.use_tnef= True
    client.send(eml)
    #ExEnd: SendMsgAsTNEF

if __name__ == '__main__':
    run()
