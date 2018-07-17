import aspose.email
from aspose.email.clients.imap import ImapClient
from aspose.email.clients import SecurityOptions
from aspose.email.clients.imap import ImapQueryBuilder
import datetime as dt

def run():
    dataDir = ""

    try:
        #ExStart:CaseSensitiveEmailsFiltering
        client = ImapClient("imap.gmail.com", 993, "username", "password")
        client.select_folder("Inbox")
        builder = ImapQueryBuilder()
        builder.subject.contains("Newsletter", True)
                
        query = builder.get_query()
        msgsColl = client.list_messages(query)
        print("Total Messages fulfilling search criterion: " + str(len(msgsColl)))
        #ExEnd:CaseSensitiveEmailsFiltering
    except Exception as ex:
        print(str(ex))

if __name__ == '__main__':
    run()
