import aspose.email as ae
from aspose.email import MailMessage, EmlLoadOptions, EmlSaveOptions, MailMessageSaveType, FileCompatibilityMode

def run():
    
    dataDir = "Data/"
    #ExStart: PreserveTnefAttachment
    # Load file
    mailMessage = MailMessage.load(dataDir + "PreserveOriginalBoundaries.eml");

    # Save as eml with preserved attachment
    emlSaveOptions = EmlSaveOptions(MailMessageSaveType.eml_format)
    emlSaveOptions.file_compatibility_mode = FileCompatibilityMode.PRESERVE_TNEF_ATTACHMENTS

    mailMessage.save(dataDir + "PreserveTNEFAttachment_out.eml", emlSaveOptions);
    #ExEnd: PreserveTnefAttachment
    
if __name__ == '__main__':
    run()
