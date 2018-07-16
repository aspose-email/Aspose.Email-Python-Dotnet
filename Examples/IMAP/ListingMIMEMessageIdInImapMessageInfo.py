import aspose.email
from aspose.email.clients.imap import ImapClient
from aspose.email.clients import SecurityOptions

def run():
    try:
    #ExStart: ListingMessagesWithPagingSupport
        with ImapClient("imap.gmail.com", 993, "username", "password") as conn:
                conn.select_folder("Inbox")
                for msg in conn.list_messages():
                    print( "From: '{}', MIME Id: {}".format(msg.from_address, msg.message_id) )
    #ExEnd: ListingMessagesWithPagingSupport
    except Exception as ex:
        print(str(ex));

if _name_ == '__main__':
    run()
