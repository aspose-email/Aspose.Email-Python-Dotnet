import aspose.email as ae
import datetime as datetime

def run():
    
    #ExStart: MailMessageFeatures
    message = ae.MailMessage()
    message.from_address = ae.MailAddress("sender@sender.com")
    message.to.append(ae.MailAddress("receiver@receiver.com", "Receiver"))
    message.subject = "Using MailMessage Features"

    # Specify message date
    message.date = datetime.datetime.now()

    # Specify message priority
    message.priority = ae.MailPriority.HIGH

    # Specify message sensitivity
    message.sensitivity = ae.MailSensitivity.NORMAL

    # Specify options for delivery notifications
    message.delivery_notification_options = ae.DeliveryNotificationOptions.ON_SUCCESS
    
    #ExEnd: MailMessageFeatures
    
if __name__ == '__main__':
    run()
