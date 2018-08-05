import aspose.email as ae
from aspose.email import MailMessage, EmlLoadOptions, HtmlLoadOptions, MhtmlLoadOptions, MsgLoadOptions

def run():
    
    dataDir = "Data/"
    #ExStart: LoadMessageWithLoadOptions
    # Load Eml, html, mhtml, msg and dat file 
    mailMessage = MailMessage.load(dataDir + "Message.eml", EmlLoadOptions())
    MailMessage.load(dataDir + "description.html",  HtmlLoadOptions())
    MailMessage.load(dataDir + "Message.mhtml", MhtmlLoadOptions())
    MailMessage.load(dataDir + "Message.msg", MsgLoadOptions())

    # loading with custom options
    emlLoadOptions = EmlLoadOptions()
    emlLoadOptions.preserve_tnef_attachments = True

    MailMessage.load(dataDir + "description.html", emlLoadOptions)
    htmlLoadOptions = HtmlLoadOptions()
    htmlLoadOptions.should_add_plain_text_view = True
    htmlLoadOptions.path_to_resources = dataDir

    MailMessage.load(dataDir + "description.html", emlLoadOptions)
    #ExEnd: LoadMessageWithLoadOptions
    
if __name__ == '__main__':
    run()
