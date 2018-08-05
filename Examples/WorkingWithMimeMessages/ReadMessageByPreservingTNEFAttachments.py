import aspose.email as ae
from aspose.email import MailMessage, MsgLoadOptions, MailMessageSaveType

def run():
    
    dataDir = "Data/"
    #ExStart: ReadMessageByPreservingTNEFAttachment
    options = MsgLoadOptions()
    options.preserve_tnef_attachments = True
    eml = MailMessage.load(dataDir + "EmbeddedImage1.msg", options)
    for attachment in eml.Attachments:
        print(attachment.name)
    #ExEnd: ReadMessageByPreservingTNEFAttachments
    
if __name__ == '__main__':
    run()
