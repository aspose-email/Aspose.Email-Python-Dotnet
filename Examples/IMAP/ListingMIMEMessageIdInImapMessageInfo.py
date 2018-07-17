import aspose.email
from aspose.email.clients.imap import ImapClient
from aspose.email.clients import SecurityOptions

def run():
    #ExStart: ListingMessagesWithPagingSupport
    conn = ImapClient("imap.gmail.com", 993, "username", "password")
    conn.select_folder("Inbox")
    for msg in conn.list_messages():
        print( "From: '{}', MIME Id: {}".format(msg.from_address, msg.message_id) )
    #ExEnd: ListingMessagesWithPagingSupport

if __name__ == '__main__':
    run()
