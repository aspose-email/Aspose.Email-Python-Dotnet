import aspose.email as ae
from aspose.email import MailMessage, EmlLoadOptions, HtmlLoadOptions, MhtmlLoadOptions, MsgLoadOptions
from aspose.email.tools import FileFormatUtil

def run():
    
    dataDir = "Data/"
    #ExStart: PreserveEmbeddedMSGFormatDuringLoad
    # Load file
    emlLoadOptions = EmlLoadOptions()
    emlLoadOptions.preserve_embedded_message_format = True
    
    mail = MailMessage.load(dataDir + "tnefWithMsgInside.eml", emlLoadOptions)

    stream = mail.attachments[0].content_stream
    
    fileFormat = FileFormatUtil.detect_file_format(stream).file_format_type;

    print(f"Embedded message file format: {fileFormat}");
    #ExEnd: PreserveEmbeddedMSGFormatDuringLoad
    
if __name__ == '__main__':
    run()
