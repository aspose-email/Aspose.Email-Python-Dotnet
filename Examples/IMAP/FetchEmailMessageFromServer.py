import aspose.email
from aspose.email.clients.imap import ImapClient
from aspose.email.clients import SecurityOptions

def run():
    dataDir = ""

    #ExStart: FetchEmailMessageFromServer
    conn = ImapClient("imap.gmail.com", 993, "username", "password")
    conn.select_folder("Inbox")
    for msg in conn.list_messages():
        conn.save_message(msg.unique_id, dataDir + msg.unique_id + "_out.eml")
    #ExEnd: FetchEmailMessageFromServer

if __name__ == '__main__':
    run()
