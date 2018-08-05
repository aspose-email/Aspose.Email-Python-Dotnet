import aspose.email as ae
from aspose.email import MailMessage, EmlLoadOptions, HtmlSaveOptions, MailMessageSaveType

def run():
    
    dataDir = "Data/"
    #ExStart: SaveMessageAsHTML
    # Load file
    message = MailMessage.load(dataDir + "Message.eml");

    message.save(dataDir + "SaveAsHTML_out.html", SaveOptions.DefaultHtml);

    #OR

    eml = MailMessage.load(dataDir + "Message.eml")
    options = SaveOptions.default_html
    options.embed_resources = False
    options.HtmlFormatOptions = HtmlFormatOptions.WriteHeader | HtmlFormatOptions.WriteCompleteEmailAddress #save the message headers to output HTML using the formatting options
    eml.save(dataDir + "SaveAsHTML1_out.html", options)
    #ExEnd: SaveMessageAsHTML
    
if __name__ == '__main__':
    run()
