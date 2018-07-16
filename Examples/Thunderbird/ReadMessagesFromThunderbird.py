import aspose.email
from aspose.email import MailMessage
from aspose.email.storage.mbox import MboxrdStorageReader

def run():
    dataDir = "Data/"
    #ExStart: ReadMessagesFromThunderbird
    reader = MboxrdStorageReader(dataDir + "ExampleMbox.mbox", False)

    eml = reader.read_next_message()

    # Read all messages in a loop
    while (eml is not None):

        # Manipulate message - show contents
        print("Subject: " + eml.subject)
        #Save this message in EML or MSG format
        eml.save(eml.subject + "_out.eml", aspose.email.SaveOptions.default_eml)
        eml.save(eml.subject + "_out.msg", aspose.email.SaveOptions.default_msg_unicode)

        # Get the next message
        eml = reader.read_next_message();

    # Close the streams
    reader.dispose();
#ExEnd: ReadMessagesFromThunderbird
if __name__ == '__main__':
    run()
