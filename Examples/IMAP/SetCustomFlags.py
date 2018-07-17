import aspose.email
from aspose.email.clients.imap import ImapClient
from aspose.email.clients.imap import ImapMessageFlags
from aspose.email.clients import SecurityOptions
from aspose.email.clients.imap import ImapFolderInfo
from aspose.email import MailMessage
    
def run():
    #ExStart: SetCustomFlags
    client = ImapClient("imap.gmail.com", 993, "username", "password")
    message = MailMessage("user@domain1.com", "user@domain2.com", "subject", "message");

    #Append the message to mailbox
    uid = client.append_message("Inbox", message);

    client.add_message_flags(uid, ImapMessageFlags.keyword("custom1"))
    #ExEnd: SetCustomFlags

if __name__ == '__main__':
    run()
