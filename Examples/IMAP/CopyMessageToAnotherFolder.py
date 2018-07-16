import aspose.email
from aspose.email.clients.imap import ImapClient
from aspose.email.clients import SecurityOptions
from aspose.email import MailMessage

def run():
    dataDir = ""

    try:
    #ExStart: CopyMessageToAnotherFolder
        with ImapClient("imap.gmail.com", 993, "username", "password") as client:
            client.select_folder("Inbox")
            folderName = "MovedMessagesToFolder"

            #List messages from Inbox to verify that messages have been copied
            msgsCollection = client.list_messages()
            print("Total Messages in Inbox before appending: " + str(len(msgsCollection)))
            
            #Append 2 new Messages to Inbox
            msg = MailMessage("user@domain1.com", "user@domain2.com", "Message1TobeMoved", "message")
            msgId1 = client.append_message(msg)
            msg2 = MailMessage("user@domain1.com", "user@domain2.com", "Message1TobeMoved", "message")
            msgId2 = client.append_message(msg2)
            
            #List messages from Inbox to verify that messages have been copied
            msgsCollection = client.list_messages()
            print("Total Messages in Inbox after appending: " + str(len(msgsCollection)))

            msgsIds = []
            msgsIds.append(msgId1)
            msgsIds.append(msgId2)
                    
            #Copy message to another folder
            client.copy_messages(msgsIds, folderName)
    #ExEnd: CopyMessageToAnotherFolder            
    except Exception as ex:
        print(str(ex))
if _name_ == '__main__':
    run()
