from aspose.email import MailMessage

def run():
    
    dataDir = "Data/"
    #ExStart: GetDecodedHeaderValues
    mailMessage = MailMessage.load(dataDir + "emlWithHeaders.eml");

    decodedValue = mailMessage.headers.get_decoded_value("Thread-Topic")

    print(decodedValue)
    #ExEnd: GetDecodedHeaderValues


if __name__ == '__main__':
    run()
