import aspose.email as ae
from aspose.email import MailMessage, EmlLoadOptions, MsgSaveOptions, MailMessageSaveType

def run():
    
    dataDir = "Data/"
    #ExStart: SavingMSGWithPreservedDates
    # Load file
    eml = MailMessage.load(dataDir + "Message.eml");

    # Save as msg with preserved dates
    msgSaveOptions = MsgSaveOptions(MailMessageSaveType.OutlookMessageFormatUnicode)
    msgSaveOptions.PreserveOriginalDates = True

    eml.save(Path.Combine(dataDir, "outTest_out.msg"), msgSaveOptions);
    #ExEnd: SavingMSGWithPreservedDates
    
if __name__ == '__main__':
    run()
