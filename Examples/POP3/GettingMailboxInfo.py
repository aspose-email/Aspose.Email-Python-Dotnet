from aspose.email.clients.pop3 import Pop3Client
from aspose.email.clients import SecurityOptions

def run():
    client = Pop3Client("pop.gmail.com", 995, "username", "password")
    client.security_options = SecurityOptions.AUTO
    #ExStart:GettingMailboxInfo
    #Get the size of the mailbox,  Get mailbox info, number of messages in the mailbox
    nSize = client.get_mailbox_size();
    print("Mailbox size is " + str(nSize) + " bytes.");
    info = client.get_mailbox_info();
    nMessageCount = info.message_count;
    print("Number of messages in mailbox are " + str(nMessageCount));
    nOccupiedSize = info.occupied_size;
    print("Occupied size is " + str(nOccupiedSize));
    #ExEnd: GettingMailboxInfo

if __name__ == '__main__':
    run()
