import aspose.email as ae
from aspose.email.clients.smtp import SmtpClient
from aspose.email.clients import SecurityOptions
from aspose.email import MailMessage
from aspose.email import AlternateView

def run():
    #ExStart: SetAlternateText
    eml = ae.MailMessage()
    eml.subject = "Message with Alternate Text"
    eml.is_body_html = True
    eml.html_body = "<html><body>This is the <b>HTML</b>body</body></html>"
    eml.from_address = "from@gmail.com"
    eml.to.append(ae.MailAddress("to@gmail.com", "Recipient 1"))

    # Creates AlternateView to view an email message using the content specified in the //string
    alternate = AlternateView.create_alternate_view_from_string("Alternate Text");
                
    # Adding alternate text
    eml.alternate_views.append(alternate)

    #Send using Smtp Client
    client = SmtpClient("smtp.gmail.com", 995, "username", "password")
    client.security_options = SecurityOptions.AUTO

    client.send(eml)
    #ExEnd: SetAlternateText

if __name__ == '__main__':
    run()
