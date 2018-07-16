import aspose.email
from aspose.email.clients.imap import ImapClient
from aspose.email.clients import SecurityOptions

def run():
    dataDir = ""

    try:
    #ExStart: RetrievingServerExtensions
        with ImapClient("imap.gmail.com", 993, "username", "password") as client:
            capabilities = client.get_capabilities()
            for val in capabilities:
                print(val);
    #ExEnd: RetrievingServerExtensions     
    except Exception as ex:
        print(str(ex))

if _name_ == '__main__':
    run()
