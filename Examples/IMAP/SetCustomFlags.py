import aspose.email
from aspose.email.clients.imap import ImapClient
from aspose.email.clients.imap import ImapMessageFlags
from aspose.email.clients import SecurityOptions
from aspose.email.clients.imap import ImapFolderInfo
from aspose.email import MailMessage
    
def run():
    try:
    #ExStart: SetCustomFlags
        with ImapClient("imap.gmail.com", 993, "username", "password") as client:
                message = MailMessage("user@domain1.com", "user@domain2.com", "subject", "message");

                #Append the message to mailbox
                uid = client.append_message("Inbox", message);

                client.add_message_flags(uid, ImapMessageFlags.keyword("custom1"))
    #ExEnd: SetCustomFlags
    except Exception as e:
        print("Error: " + str(e));

if _name_ == '__main__':
    run()
