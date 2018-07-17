from aspose.email import MailMessage
from aspose.email import Attachment
from aspose.email import SaveOptions

def run():
    dataDir = "Data/"
    #ExStart: ExtractEmbeddedObjectsFromEmail    
    # Create an instance of MailMessage class
    message = MailMessage.load(dataDir + "EmailWithAttandEmbedded.eml")

    # Save attachments from message
    for index, att in enumerate(message.attachments):
        att.save(dataDir + att.name)
    #ExEnd: ExtractEmbeddedObjectsFromEmail


if __name__ == '__main__':
    run()
