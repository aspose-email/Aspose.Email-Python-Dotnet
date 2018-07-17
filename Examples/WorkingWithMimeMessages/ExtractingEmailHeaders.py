from aspose.email import MailMessage

def run():    
    dataDir = "Data/"
    #ExStart: ExtractingEmailHeaders
    # Create MailMessage instance by loading an EML file
    message = MailMessage.load(dataDir + "email-headers.eml");
    print("\n\nheaders:\n\n")

    # Print out all the headers
    index = 0
    for index, header in enumerate(message.headers):
        print(header + " - ", end=" ")
        print (message.headers.get(index))
    #ExEnd:ExtractingEmailHeaders

if __name__ == '__main__':
    run()

        
