import aspose.email as ae
import datetime as datetime

def run():
    
    #ExStart: MailMessageFeatures
    message = ae.MailMessage()
    message.from_address = "sender@sender.com"
    message.to.append(ae.MailAddress("receiver@receiver.com", "Receiver"))
    message.subject = "Using MailMessage Features"

    # Specify message date
    message.date = datetime.datetime.now()

    # Specify message priority
    message.priority = ae.MailPriority.HIGH

    # Specify message sensitivity
    message.Sensitivity = ae.MailSensitivity.NORMAL

    # Specify options for delivery notifications
    message.DeliveryNotificationOptions = ae.DeliveryNotificationOptions.ON_SUCCESS
    
    #ExEnd: MailMessageFeatures
    
if __name__ == '__main__':
    run()
