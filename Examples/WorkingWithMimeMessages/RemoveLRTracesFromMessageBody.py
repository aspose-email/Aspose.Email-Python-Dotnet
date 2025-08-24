from aspose.email import MailMessage
from aspose.email import Attachment
from aspose.email import SaveOptions

def run():
    dataDir = "Data/"
    #ExStart: RemoveLRTracesFromMessageBody     
    # Create an instance of MailMessage class
    message = MailMessage.load(dataDir + "EmailWithAttandEmbedded.eml")

    message.linked_resources.remove_at(0, True)

    message.alternate_views[0].linked_resources.clear()

    message.save(dataDir + "RemoveLRTracesFromMessageBody_out.eml")
    #ExEnd: RemoveLRTracesFromMessageBody

if __name__ == '__main__':
    run()
