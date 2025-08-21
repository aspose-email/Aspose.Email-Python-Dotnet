import aspose.email
from aspose.email import MailMessage
from aspose.email.storage.mbox import MboxrdStorageReader
from aspose.email.storage.mbox import MboxLoadOptions


def run():
    dataDir = "Data/"
    #ExStart: GetNumberOfItemsFromMBox
    reader = MboxrdStorageReader(dataDir + "ExampleMbox.mbox", MboxLoadOptions())
    print("Total items in MBox file: " + str(reader.get_total_items_count()))
    #ExEnd: GetNumberOfItemsFromMBox
if __name__ == '__main__':
    run()
