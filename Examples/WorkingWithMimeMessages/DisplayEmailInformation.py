from aspose.email import MailMessage

def run():
    dataDir = ""
    #ExStart: DisplayEmailInformation
    # Create MailMessage instance by loading an Eml file
    message = MailMessage.load(dataDir + "test.eml")

    # Gets the sender info, recipient info, Subject, htmlbody and textbody
    print("Subject: " + message.subject)

    print("HtmlBody: " + message.html_body)

    print("TextBody: " + message.body)
    #ExEnd: DisplayEmailInformation


if __name__ == '__main__':
    run()
