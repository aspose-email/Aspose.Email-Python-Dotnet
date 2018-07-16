from aspose.email import MailMessage
from aspose.email import Attachment
from aspose.email import SaveOptions

def run():
    dataDir = ""
    #ExStart: DetermineAttachmendEmbeddedMessage
    # Create an instance of MailMessage class
    message = MailMessage.load("EmailWithAttandEmbedded.eml")

    # Save attachments from message
    for index, att in enumerate(message.attachments):
        if att.is_embedded_message:
            print("Attachment is an embedded message")
        else:
            print("Attachment is not an embedded message")
    #ExEnd: DetermineAttachmendEmbeddedMessage

if __name__ == '__main__':
    run()

        
