import aspose.email as ae

def run():
    
    dataDir = "Data/";
    #ExStart: CreateNewMailMesssage
    eml = ae.MailMessage()
    eml.subject = "New MailMessage created with Aspose.Email for Python"
    eml.html_body = "<b>This line is in bold </b> while this is normal text"
    eml.from_address = ae.MailAddress("from@domain.com")

    eml.to.append(ae.MailAddress("to1@domain.com", "Recipient 1"))
    eml.to.append(ae.MailAddress("to2@domain.com", "Recipient 2"))

    eml.cc.append(ae.MailAddress("cc1@domain.com", "Recipient 3"))
    eml.cc.append(ae.MailAddress("cc2@domain.com", "Recipient 4"))

    #Save generated EML in different formats to disc
    eml.save(dataDir + "CreateNewMailMessage_out.eml")
    eml.save(dataDir + "CreateNewMailMessage_out.msg", ae.SaveOptions.default_msg_unicode)
    eml.save(dataDir + "message_out.msg", ae.SaveOptions.default_msg)
    eml.save(dataDir + "message_out.mhtml", ae.SaveOptions.default_mhtml)
    eml.save(dataDir + "message_out.html", ae.SaveOptions.default_html)
    #ExEnd: CreateNewMailMesssage
    
if __name__ == '__main__':
    run()
