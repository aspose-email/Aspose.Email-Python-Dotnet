import os
import aspose.email as ae
from aspose.email import MailMessage, EmlLoadOptions, MhtSaveOptions, MailMessageSaveType, SaveOptions

def run():
    
    dataDir = "Data/"
    #ExStart: ConvertToMHTMLWithoutInlineImages
    # Load file
    eml = MailMessage.load(dataDir + "Message.eml")

    options = MhtSaveOptions()
    options.skip_inline_images = True

    eml.save(os.path.join(dataDir, "outTest_out.msg"), SaveOptions.default_mhtml)
    #ExEnd: ConvertToMHTMLWithoutInlineImages
    
if __name__ == '__main__':
    run()
