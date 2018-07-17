import aspose.email
from aspose.email.clients.imap import ImapClient
from aspose.email.clients import SecurityOptions

def run():
    #ExStart: ListingMessagesRecursively
    conn =  ImapClient("imap.gmail.com", 993, "username", "password")
    conn.select_folder("Inbox")
    msgsColl = conn.list_messages(True);
    print("Total Messages: " + str(len(msgsColl)))
    #ExEnd: ListingMessagesRecursively

if __name__ == '__main__':
    run()
