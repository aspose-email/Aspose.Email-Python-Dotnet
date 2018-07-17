import aspose.email
from aspose.email.clients.imap import ImapClient
from aspose.email.clients.imap import ImapMessageFlags
from aspose.email.clients import SecurityOptions

def run():

    #ExStart: SettingMessageFlags
    conn = ImapClient("imap.gmail.com", 993, "username", "password")
    conn.select_folder("Inbox")
    conn.change_message_flags(1, ImapMessageFlags.is_read)

    conn.remove_message_flags(1, ImapMessageFlags.is_read)
    #ExEnd: SettingMessageFlags

if __name__ == '__main__':
    run()
