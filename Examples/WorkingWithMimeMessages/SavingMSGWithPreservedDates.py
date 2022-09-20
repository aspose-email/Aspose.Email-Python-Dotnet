import aspose.email as ae
from aspose.email import MailMessage, EmlLoadOptions, MsgSaveOptions, MailMessageSaveType

def run():
    
    dataDir = "Data/"
    #ExStart: SavingMSGWithPreservedDates
    # Load file
    eml = MailMessage.load(dataDir + "Message.eml");

    # Save as msg with preserved dates
    msgSaveOptions = MsgSaveOptions(MailMessageSaveType.outlook_message_format_unicode)
    msgSaveOptions.preserve_original_dates = True

    eml.save(dataDir + "outTest_out.msg", msgSaveOptions)
    #ExEnd: SavingMSGWithPreservedDates
    
if __name__ == '__main__':
    run()
