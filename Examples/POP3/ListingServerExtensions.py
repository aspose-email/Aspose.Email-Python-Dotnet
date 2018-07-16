from aspose.email.clients.pop3 import Pop3Client
from aspose.email.clients import SecurityOptions

def run():
    #ExStart: ListingServerExtensions
    client = Pop3Client("pop.gmail.com", 995, "username", "password")
    client.security_options = SecurityOptions.AUTO
    capabilities = client.get_capabilities()
    for val in capabilities:
            print(val);
    #ExEnd: ListingServerExtensions


if __name__ == '__main__':
    run()
