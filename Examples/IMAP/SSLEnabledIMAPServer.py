import aspose.email
from aspose.email.clients.imap import ImapClient
from aspose.email.clients import SecurityOptions

def run():
    try:
    #ExStart: SSLEnabledIMAPServer
    client = ImapClient("imap.domain.com", 993, "user@domain.com", "pwd")
    client.security_options = SecurityOptions.SSLIMPLICIT
    #ExEnd:SSLEnabledIMAPServer
    except Exception as e:
        print("Error: " + str(e));

if _name_ == '__main__':
    run()
