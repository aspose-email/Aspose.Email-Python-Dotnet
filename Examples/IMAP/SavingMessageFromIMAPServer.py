import aspose.email
from aspose.email.clients.imap import ImapClient
from aspose.email.clients import SecurityOptions

def run():
    dataDir = ""

    try:
    #ExStart: SavingMessageFromIMAPServer
        with ImapClient("imap.gmail.com", 993, "username", "password") as conn:
                conn.select_folder("Inbox")
                for msgInfo in conn.list_messages():
                    msg = conn.fetch_message(msgInfo.unique_id)
                    msg.save(dataDir + msgInfo.unique_id + "_out.msg", aspose.email.SaveOptions.default_msg_unicode)
    #ExEnd: SavingMessageFromIMAPServer
    except Exception as ex:
        print(str(ex))

if _name_ == '__main__':
    run()
