from aspose.email.clients.pop3 import Pop3Client
from aspose.email.clients import SecurityOptions

def run():
    #ExStart: SaveToDiscWithoutParsing
    client = Pop3Client("pop.gmail.com", 995, "username", "password")
    client.security_options = SecurityOptions.AUTO
    try:
        # Save message to disk by message sequence number
        client.save_message(1, "SaveToDiscWithoutParsing_out.eml")
        client.dispose()

    except Exception as ex:
        print(str(ex))
    #ExEnd: SaveToDiscWithoutParsing

if __name__ == '__main__':
    run()
