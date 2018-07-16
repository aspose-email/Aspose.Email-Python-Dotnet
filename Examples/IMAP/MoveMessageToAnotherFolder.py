import aspose.email
from aspose.email.clients.imap import ImapClient
from aspose.email.clients import SecurityOptions
from aspose.email import MailMessage
def run():
    
    dataDir = ""

    try:
    #ExStart: MoveMessageToAnotherFolder
        with ImapClient("imap.gmail.com", 993, "username", "password") as client:
            client.select_folder("Inbox")
            folderName = "N1Renamed"

            #Append a new Message to Inbox
            msg = MailMessage("user@domain1.com", "user@domain2.com", "subject", "message")
            msgId = client.append_message( msg)
            
            #List messages from Inbox
            msgsCollection = client.list_messages()
            print("Total Messages in Inbox: " + str(len(msgsCollection)))

            #Move message to another folder
            client.move_message(msgId, folderName)

            #List messages from Inbox
            msgsCollection = client.list_messages()
            print("Total Messages in Inbox: " + str(len(msgsCollection)))
    #ExEnd: MoveMessageToAnotherFolder            
    except Exception as ex:
        print(str(ex))

if _name_ == '__main__':
    run()
