import aspose.email as ae
from aspose.email.clients.smtp import SmtpClient
from aspose.email.clients import SecurityOptions
from aspose.email import MailMessage
from aspose.email import MailMessageCollection

def run():
    #ExStart: SendingBulkEmails
    message1 = MailMessage("from@gmail.com", "to@gmail.com", "Sending Bulk Emails using Aspose.Email", "message1, how are you?")
    message2 = MailMessage("from@gmail.com", "to@gmail.com", "Sending Bulk Emails using Aspose.Email", "message2, how are you?")
    message3 = MailMessage("from@gmail.com", "to@gmail.com", "Sending Bulk Emails using Aspose.Email", "message3, how are you?")

    manyMsg =  MailMessageCollection()
    manyMsg.append(message1)
    manyMsg.append(message2)
    manyMsg.append(message3)

    #Send using Smtp Client
    client = SmtpClient("smtp.gmail.com", 995, "username", "password")
    client.security_options = SecurityOptions.AUTO

    client.send(manyMsg)
    #ExEnd: SendingBulkEmails

if __name__ == '__main__':
    run()
