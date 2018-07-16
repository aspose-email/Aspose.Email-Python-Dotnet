from aspose.email.clients.pop3 import Pop3Client
from aspose.email.clients import SecurityOptions

def run():
    #ExStart: RetrievingEmailHeaders
    client = Pop3Client("pop.gmail.com", 995, "username", "password")
    client.security_options = SecurityOptions.AUTO    
    headers = client.get_message_headers(1)
    for index, header in enumerate(headers):
        print(header + " - ", end=" ")
        print (headers.get(index))
    #ExEnd: RetrievingEmailHeaders

if __name__ == '__main__':
    run()
