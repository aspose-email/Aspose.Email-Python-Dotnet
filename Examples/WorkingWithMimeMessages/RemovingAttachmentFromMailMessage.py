from aspose.email import MailMessage
from aspose.email import Attachment
from aspose.email import SaveOptions

def run():
    dataDir = ""
    #ExStart: RemovingAttachmentFromMailMessage
    # Create an instance of MailMessage class
    message = MailMessage("sender@domain.com", "receiver@domain.com")

    # Load an attachment
    attachment = Attachment(dataDir + "1.txt");

    # Add Multiple Attachment in instance of MailMessage class and Save message to disk
    message.attachments.append(attachment)

    print("Attachments count before removing: " + str(len(message.attachments)))

    message.attachments.remove(attachment)

    print("Attachments count after removing: " + str(len(message.attachments)))   
    #ExEnd: RemovingAttachmentFromMailMessage

if __name__ == '__main__':
    run()
