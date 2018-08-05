import aspose.email as ae
from aspose.email.tools import FileFormatUtil

def run():
    
    dataDir = "Data/";
    #ExStart: DetectDifferentFileFormats
    # Detect file format and Gets the detected load format
    info = FileFormatUtil.detect_file_format(dataDir + "message.msg")
    print("The message format is: " + info.file_format_type)
    #ExEnd: DetectDifferentFileFormats
    
if __name__ == '__main__':
    run()
