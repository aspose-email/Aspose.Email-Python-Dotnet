import aspose.email
from aspose.email.clients.imap import ImapClient
from aspose.email.clients import SecurityOptions

def run():
    try:
    #ExStart: ListingMessagesRecursively
        with ImapClient("imap.gmail.com", 993, "username", "password") as conn:
                conn.select_folder("Inbox")
                msgsColl = conn.list_messages(True);
                print("Total Messages: " + str(len(msgsColl)))
    #ExEnd: ListingMessagesRecursively
    except Exception as e:
        print("Error: " + str(e));

if _name_ == '__main__':
    run()
