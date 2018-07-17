import aspose.email
from aspose.email.clients.imap import ImapClient
from aspose.email.clients import SecurityOptions

def run():
    dataDir = ""

    #ExStart: RetrievingServerExtensions
    client= ImapClient("imap.gmail.com", 993, "username", "password")
    capabilities = client.get_capabilities()
    for val in capabilities:
        print(val);
    #ExEnd: RetrievingServerExtensions

if __name__ == '__main__':
    run()
