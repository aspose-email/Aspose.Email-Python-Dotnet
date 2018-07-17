from aspose.email import MailMessage
from aspose.email import Attachment
from aspose.email import SaveOptions

def run():
    dataDir = "Data/"
    #ExStart: DisplayAttachmentFileName
    # Create an instance of MailMessage class
    message = MailMessage.load(dataDir + "EmailWithAttandEmbedded.eml")

    # Print attachments information
    for index, att in enumerate(message.attachments):
        print(att.name)
    #ExEnd: DisplayAttachmentFileName

if __name__ == '__main__':
    run()
