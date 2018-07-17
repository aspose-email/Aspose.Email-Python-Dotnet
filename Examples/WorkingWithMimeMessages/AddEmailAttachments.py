from aspose.email import MailMessage
from aspose.email import Attachment
from aspose.email import SaveOptions

def run():

    dataDir = "Data/"
    #ExStart: AddEmailAttachments             
    # Create an instance of MailMessage class
    message = MailMessage("sender@domain.com", "receiver@domain.com")

    # Load an attachment
    attachment = Attachment(dataDir + "1.txt");

    # Add Multiple Attachment in instance of MailMessage class and Save message to disk
    message.attachments.append(attachment);           
    message.add_attachment(Attachment(dataDir + "1.jpg"))
    message.add_attachment(Attachment(dataDir + "1.doc"))
    message.add_attachment(Attachment(dataDir + "1.rar"))
    message.add_attachment(Attachment(dataDir + "1.pdf"))
    message.save(dataDir + "AddEmailAttachments_out.msg", SaveOptions.default_msg_unicode)
    #ExEnd: AddEmailAttachments


if __name__ == '__main__':
    run()
