import aspose.email as ae
from aspose.email import MailMessage, EmlLoadOptions, HtmlSaveOptions, MailMessageSaveType, SaveOptions, HtmlFormatOptions, ResourceRenderingMode

def run():
    
    dataDir = "Data/"
    #ExStart: SaveMessageAsHTML
    # Load file
    message = MailMessage.load(dataDir + "Message.eml")

    message.save(dataDir + "SaveAsHTML_out.html", SaveOptions.default_html)

    #OR

    eml = MailMessage.load(dataDir + "Message.eml")
    options = SaveOptions.default_html
    options.resource_rendering_mode = ResourceRenderingMode.NONE
    options.html_format_options = HtmlFormatOptions.WRITE_HEADER | HtmlFormatOptions.WRITE_COMPLETE_EMAIL_ADDRESS #save the message headers to output HTML using the formatting options
    eml.save(dataDir + "SaveAsHTML1_out.html", options)
    #ExEnd: SaveMessageAsHTML
    
if __name__ == '__main__':
    run()
