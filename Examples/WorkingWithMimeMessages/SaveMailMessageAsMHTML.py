import aspose.email as ae
from aspose.email import MailMessage, EmlLoadOptions, MsgSaveOptions, MailMessageSaveType

def run():
    
    dataDir = "Data/"
    #ExStart: SaveMailMessageAsMHTML
    # Load file
    eml = MailMessage.load(dataDir + "Message.eml")

    eml.save(Path.Combine(dataDir, "outTest_out.msg"), SaveOptions.default_mhtml)
    #ExEnd: SaveMailMessageAsMHTML
    
if __name__ == '__main__':
    run()
