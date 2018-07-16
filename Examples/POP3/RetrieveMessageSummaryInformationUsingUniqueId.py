from aspose.email.clients.pop3 import Pop3Client
from aspose.email.clients import SecurityOptions

def run():
    #ExStart: RetrieveMessageSummaryInformationUsingUniqueId    
    client = Pop3Client("pop.gmail.com", 995, "username", "password")
    client.security_options = SecurityOptions.AUTO

    uniqueId = "unique id of a message from server"

    messageInfo = client.get_message_info(uniqueId)

    if messageInfo is not None:
        print(messageInfo.subject)
        print(messageInfo.date)
    #ExEnd: RetrieveMessageSummaryInformationUsingUniqueId

if __name__ == '__main__':
    run()
