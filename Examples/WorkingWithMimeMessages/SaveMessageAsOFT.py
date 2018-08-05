import aspose.email as ae
from aspose.email import MailMessage, EmlLoadOptions, SaveOptions, MailMessageSaveType

def run():
    
    dataDir = "Data/"
    #ExStart: SaveMessageAsOFT
    # Load file
    eml =MailMessage("test@from.to", "test@to.to", "template subject", "Template body")
    oftEmlFileName = "EmlAsOft_out.oft"
    options = SaveOptions.default_msg_unicode
    options.save_as_template = True
    eml.save(dataDir + oftEmlFileName, options)
    #ExEnd: SaveMessageAsOFT
    
if __name__ == '__main__':
    run()
