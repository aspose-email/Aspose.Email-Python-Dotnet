from aspose.email import MailMessage
from aspose.email import Attachment
from aspose.email import SaveOptions

def run():
    dataDir = ""
    #ExStart: RemoveLRTracesFromMessageBody     
    # Create an instance of MailMessage class
    message = MailMessage.load("EmailWithAttandEmbedded.eml")

    message.linked_resources.remove_at(0, True)

    message.alternate_views[0].linked_resources.clear(True)

    message.save("RemoveLRTracesFromMessageBody_out.eml")
    #ExEnd: RemoveLRTracesFromMessageBody

if __name__ == '__main__':
    run()
