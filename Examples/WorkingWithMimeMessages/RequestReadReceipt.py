import aspose.email as ae

def run():
    
    #ExStart:RequestReadReceipt
    # Create an Instance of MailMessage class
    message = ae.MailMessage()
    message.from_address = ae.MailAddress("sender@sender.com")
    message.to.append(ae.MailAddress("receiver@receiver.com", "Receiver"))
    message.subject = "Using MailMessage Features"
    message.html_body = "<html><body>This is the Html body</body></html>"
    message.delivery_notification_options = ae.DeliveryNotificationOptions.ON_SUCCESS
    message.headers.add("Return-Receipt-To", "sender@sender.com")
    message.headers.add("Disposition-Notification-To", "sender@sender.com")

    # Create an instance of SmtpClient Class and specify your mailing Host server, Username, Password and Port No
    client = ae.clients.smtp.SmtpClient("smtp.gmail.com", 995, "username", "password")
    
    try:
        # Client.Send will send this message
        client.send(message)

        # Display ‘Message Sent’, only if message sent successfully
        print("Message sent")
    except:
        print("Some Error Occured!")

    #ExEnd: RequestReadReceipt
    
if __name__ == '__main__':
    run()
