from aspose.email.clients.pop3 import Pop3Client
from aspose.email.clients import SecurityOptions

def run():

    #ExStart: DeleteEmailByIndex
    client = Pop3Client("imap.gmail.com", 993, "username", "password")
    client.security_options = SecurityOptions.AUTO

    # Delete all the message one by one
    messageCount = client.get_message_count()

    print("Total messages in inbox: " + str(messageCount))

    for i in range(1,messageCount):
        client.delete_message(i)

    client.commit_deletes()
    #ExEnd: DeleteEmailByIndex  


if __name__ == '__main__':
    run()
