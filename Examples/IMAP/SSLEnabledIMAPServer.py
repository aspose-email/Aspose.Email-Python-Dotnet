import aspose.email
from aspose.email.clients.imap import ImapClient
from aspose.email.clients import SecurityOptions

def run():
    #ExStart: SSLEnabledIMAPServer
    client = ImapClient("imap.domain.com", 993, "user@domain.com", "pwd")
    client.security_options = SecurityOptions.SSLIMPLICIT
    #ExEnd:SSLEnabledIMAPServer

if __name__ == '__main__':
    run()
