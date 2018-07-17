from aspose.email.clients.pop3 import Pop3Client
from aspose.email.clients import SecurityOptions

def run():
    #ExStart: GetEmailCountInMailbox    
    client = Pop3Client("pop.gmail.com", 995, "username", "password")
    client.security_options = SecurityOptions.AUTO
    #Get the size of the mailbox,  Get mailbox info, number of messages in the mailbox
    i = client.get_message_count();
    print("No. of emails: " + str(i));
    #ExEnd: GetEmailCountInMailbox

if __name__ == '__main__':
    run()
