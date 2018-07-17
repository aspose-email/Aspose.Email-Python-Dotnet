from aspose.email.clients.pop3 import Pop3Client
from aspose.email.clients import SecurityOptions

def run():
    #ExStart: ConnectingToPOP3
    client = Pop3Client()
    # Specify host, username, password, Port and SecurityOptions for your client
    client.host = "pop.gmail.com";
    client.username = "your.username@gmail.com";
    client.password = "your.password";
    client.port = 995;
    client.security_options = SecurityOptions.AUTO;
    print("Connected to POP3 server.");
    #ExEnd: ConnectingToPOP3


if __name__ == '__main__':
    run()
