import aspose.email
from aspose.email.clients.imap import ImapClient
from aspose.email.clients import SecurityOptions
from aspose.email import MailMessage
def run():
    
    dataDir = ""

    #ExStart: MoveMessageToAnotherFolder
    client = ImapClient("imap.gmail.com", 993, "username", "password")
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

if __name__ == '__main__':
    run()
