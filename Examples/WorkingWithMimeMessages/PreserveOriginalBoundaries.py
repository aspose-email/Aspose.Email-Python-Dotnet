import aspose.email as ae
from aspose.email import MailMessage, EmlLoadOptions, EmlSaveOptions, MailMessageSaveType

def run():
    
    dataDir = "Data/"
    #ExStart: PreserveOriginalBoundaries
    # Load file
    mailMessage = MailMessage.load(dataDir + "Attachments.eml");

    # Save as eml with preserved original boundares
    emlSaveOptions = EmlSaveOptions(MailMessageSaveType.eml_format)
    #emlSaveOptions.preserve_original_boundaries = True

    mailMessage.save(dataDir + "PreserveOriginalBoundaries_out.eml", emlSaveOptions);
    #ExEnd: PreserveOriginalBoundaries
    
if __name__ == '__main__':
    run()
