from aspose.email.clients.pop3 import Pop3Client
from aspose.email.clients import SecurityOptions

def run():
    #ExStart: SSLEnabledPOP3Server
    client = Pop3Client()
    # Specify host, username and password, Port and  SecurityOptions for your client
    client.host = "pop.gmail.com"
    client.username = "your.username@gmail.com"
    client.password = "your.password"
    client.port = 995
    client.security_options = SecurityOptions.SSLEXPLICIT;
    print("Connecting to POP3 server using SSL.")
    #ExEnd: SSLEnabledPOP3Server


if __name__ == '__main__':
    run()
