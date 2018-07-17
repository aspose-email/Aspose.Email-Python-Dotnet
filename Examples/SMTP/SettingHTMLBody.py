import aspose.email as ae
from aspose.email.clients.smtp import SmtpClient
from aspose.email.clients import SecurityOptions
from aspose.email import MailMessage

def run():
    #ExStart: SettingHTMLBody
    eml = ae.MailMessage()
    eml.subject = "Message with Html Body"
    eml.is_body_html = True
    eml.html_body = "<html><body>This is the <b>HTML</b>body</body></html>"
    eml.from_address = "from@gmail.com"
    eml.to.append(ae.MailAddress("to@gmail.com", "Recipient 1"))

    #Send using Smtp Client
    client = SmtpClient("smtp.gmail.com", 995, "username", "password")
    client.security_options = SecurityOptions.AUTO

    client.send(eml)
    #ExEnd: SettingHTMLBody

if __name__ == '__main__':
    run()
