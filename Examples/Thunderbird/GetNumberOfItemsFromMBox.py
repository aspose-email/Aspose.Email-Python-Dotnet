import aspose.email
from aspose.email import MailMessage
from aspose.email.storage.mbox import MboxrdStorageReader

def run():
    dataDir = "Data/"
    #ExStart: GetNumberOfItemsFromMBox
    reader = MboxrdStorageReader(dataDir + "ExampleMbox.mbox", False)
    print("Total items in MBox file: " + str(reader.get_total_items_count()))
    #ExEnd: GetNumberOfItemsFromMBox
if __name__ == '__main__':
    run()
