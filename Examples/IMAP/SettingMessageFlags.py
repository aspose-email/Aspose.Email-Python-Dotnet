import aspose.email
from aspose.email.clients.imap import ImapClient
from aspose.email.clients.imap import ImapMessageFlags
from aspose.email.clients import SecurityOptions

def run():
    try:
    #ExStart: SettingMessageFlags
        with ImapClient("imap.gmail.com", 993, "username", "password") as conn:
                conn.select_folder("Inbox")
                conn.change_message_flags(1, ImapMessageFlags.is_read)

                conn.remove_message_flags(1, ImapMessageFlags.is_read)
    #ExEnd: SettingMessageFlags
    except Exception as e:
        print("Error: " + str(e));

if _name_ == '__main__':
    run()
