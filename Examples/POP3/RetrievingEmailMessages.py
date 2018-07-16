from aspose.email.clients.pop3 import Pop3Client
from aspose.email.clients import SecurityOptions

def run():
    #ExStart: RetrievingEmailMessages
    client = Pop3Client("pop.gmail.com", 995, "username", "password")
    client.security_options = SecurityOptions.AUTO

    messageCount = client.get_message_count();

    print("Total messages: " + str(messageCount))
    #Create an instance of the MailMessage class and Retrieve message    
    for i in range(0,messageCount):
        message = client.fetch_message(i+1)
        print("From:" + str(message.from_address))
        print("Subject:" + message.subject)
        print(message.html_body);

    #ExEnd: RetrievingEmailMessages

if __name__ == '__main__':
    run()
