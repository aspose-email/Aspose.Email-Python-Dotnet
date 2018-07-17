from aspose.email import MailMessage
from aspose.email import MailAddress
from aspose.email import SaveOptions

def run():    
    dataDir = "Data/"
    #ExStart:ChangeEmailAddress
    message = MailMessage();

    message.subject = "Creating Message with Friendly Email Address."

    # A To address with a friendly name can also be specified like this
    message.to.append(MailAddress("kyle@to.com", "Kyle Huang"))

    # Specify Cc and Bcc email address along with a friendly name
    message.cc.append(MailAddress("guangzhou@cc.com", "Guangzhou Team"))
    message.bcc.append(MailAddress("ahaq@bcc.com", "Ammad ulHaq "))

    message.save(dataDir + "MessageWithFrienlyName_out.eml", SaveOptions.default_eml)
    #ExEnd: ChangeEmailAddress


if __name__ == '__main__':
    run()
