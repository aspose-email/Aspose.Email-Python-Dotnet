import aspose.email
from aspose.email.clients.imap import ImapClient
from aspose.email.clients import SecurityOptions

def run():
    dataDir = ""

    try:
    #ExStart: FetchEmailMessageFromServer
        with ImapClient("imap.gmail.com", 993, "username", "password") as conn:
                conn.select_folder("Inbox")
                for msg in conn.list_messages():
                    conn.save_message(msg.unique_id, dataDir + msg.unique_id + "_out.eml")
    #ExEnd: FetchEmailMessageFromServer
    except Exception as ex:
        print(str(ex))

if _name_ == '__main__':
    run()
