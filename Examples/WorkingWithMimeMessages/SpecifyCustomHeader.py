import aspose.email as ae

def run():
    #ExStart: SpecifyCustomHeader
    # Create an instance of MailMessage class
    eml = ae.MailMessage()
    
    # Specify ReplyTo, From, To field, Cc and Bcc Addresses
    eml.reply_to_list.Add("reply@reply.com")
    eml.from_address = "sender@sender.com"
    eml.to.append(ae.MailAddress("to1@domain.com", "Recipient 1"))
    eml.subject = "test mail"
    eml.headers.Add("secret-header", "mystery")
    
    client = ae.clients.smtp.SmtpClient("smtp.gmail.com", 995, "username", "password")
    
    try:
        # Client.Send will send this message
        client.send(eml)

        # Display ‘Message Sent’, only if message sent successfully
        print("Message sent")
    except:
        print("Some Error Occured!")

    #ExEnd: SpecifyCustomHeader

if __name__ == '__main__':
    run()

