import aspose.email
from aspose.email.clients.imap import ImapClient
from aspose.email.clients import SecurityOptions
from aspose.email import MailMessage

def run():
    dataDir = ""

    try:
    #ExStart: DeleteMultipleMessages
        with ImapClient("imap.gmail.com", 993, "username", "password") as client:

                print(client.uid_plus_supported)

                #Append some test messages
                client.select_folder("Inbox")
                uidList = []

                messageInfoCol = client.list_messages()
                print("Total messages in Inbox before appending: " + str(len(messageInfoCol)))

                #No. of messages to be appended
                messageNumber = 2

                message = MailMessage("from@Aspose.com", "to@Aspose.com", "Message 1", "Add ability in ImapClient to delete message")
                emailId = client.append_message(message)
                uidList.append(emailId)

                message = MailMessage("from@Aspose.com", "to@Aspose.com", "Message 2", "Add ability in ImapClient to delete message")
                emailId = client.append_message(message)
                uidList.append(emailId)

                #Now verify that all the messages have been appended to the mailbox
                messageInfoCol = client.list_messages()
                print("Total messages in Inbox after appending: " + str(len(messageInfoCol)))

                client.delete_messages(uidList, True)
                client.commit_deletes()
                messageInfoCol = client.list_messages()
                print("Total messages in Inbox after deletion: " + str(len(messageInfoCol)))
    #ExEnd: DeleteMultipleMessages            
    except Exception as ex:
        print(str(ex))

if _name_ == '__main__':
    run()
