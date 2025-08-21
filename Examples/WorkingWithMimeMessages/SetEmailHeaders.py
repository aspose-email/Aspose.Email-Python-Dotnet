import aspose.email as ae
import datetime

def run():
    # The path to the File directory.
    dataDir = "Data/"

    #ExStart: SetEmailHeaders
    # Create an instance of MailMessage class
    eml = ae.MailMessage()
    
    # Specify ReplyTo, From, To field, Cc and Bcc Addresses
    eml.reply_to_list.append(ae.MailAddress("reply@reply.com"))
    eml.from_address = ae.MailAddress("sender@sender.com")
    eml.to.append(ae.MailAddress("to1@domain.com", "Recipient 1"))
    eml.to.append(ae.MailAddress("to2@domain.com", "Recipient 2"))
    eml.cc.append(ae.MailAddress("cc@domain.com", "Recipient 3"))
    eml.bcc.append(ae.MailAddress("bcc@domain.com", "Recipient 4"))

    # Specify Date, Message subject, XMailer, Secret Header, Save message to disc
    eml.subject = "test mail"
    eml.date = datetime.datetime(2006, 3, 6, 12, 00)
    eml.x_mailer = "Aspose.Email"
    eml.headers.add("secret-header", "mystery")
    eml.save(dataDir + "SetEmailHeaders_out.msg", ae.SaveOptions.default_msg)
    #ExEnd: SetEmailHeaders

if __name__ == '__main__':
    run()

