import aspose.email
from aspose.email.clients.imap import ImapClient
from aspose.email.clients import SecurityOptions
from aspose.email import MailMessage
from aspose.email.clients.imap import ImapMessageInfo
def run():

    dataDir = ""

    #ExStart: RetreiveExtraParametersAsSummaryInformation
    client = ImapClient("imap.gmail.com", 993, "username", "password")
    client.select_folder("Inbox")
    msg = MailMessage("user@domain1.com", "user@domain2.com", "subject", "message")
    client.subscribe_folder(client.current_folder.name)
    uid = client.append_message(client.current_folder.name, msg)

    messageExtraFields = ["X-GM-MSGID", "X-GM-THRID"]

    #retreive the message summary information using it's UID
    messageInfoUID = client.list_message(uid, messageExtraFields)

    #retreive the message summary information using it's sequence number
    messageInfoSeqNum = client.list_message(1, messageExtraFields)

    #List messages in general from the server based on the defined properties
    messageInfoCol = client.list_messages(messageExtraFields)

    print(str(len(messageInfoCol)))
    messageInfoFromList = messageInfoCol[0]

    if messageInfoFromList.extra_parameters is not None:
        for paramName in messageExtraFields:
            print(messageInfoFromList.extra_parameters.has_key(paramName))
    #ExEnd: RetreiveExtraParametersAsSummaryInformation  

if __name__ == '__main__':
    run()
