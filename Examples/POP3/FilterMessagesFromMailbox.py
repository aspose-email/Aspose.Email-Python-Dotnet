from aspose.email.clients.pop3 import Pop3Client
from aspose.email.clients import SecurityOptions
from aspose.email.tools.search import MailQueryBuilder 
import datetime as dt
from datetime import timedelta

def run():
    #ExStart: FilterMessagesFromMailbox   
    client = Pop3Client("pop.gmail.com", 995, "username", "password")
    client.security_options = SecurityOptions.AUTO
 
    builder = MailQueryBuilder()

    #Filtering on Subject
    builder.subject.contains("Newsletter")

    #Filtering on Internal Date
    builder.internal_date.on(dt.datetime.now())

    #Filtering on Date Range
    builder.internal_date.before(dt.datetime.now())
    builder.internal_date.since(dt.datetime.today() - timedelta(days=7))

    #Filtering on Sender
    builder.from_address.contains("saqib.razzaq@127.0.0.1")

    #Filtering on Specific Domain
    builder.from_address.contains("SpecificHost.com");
    
    #Filtering on specific Recipient
    builder.to.contains("recipient")

    #Combining Queries with OR
    #builder.either(builder.subject.contains("test"), builder.from_address.contains("noreply@host.com"))

    #Case-Sensitive Email Filtering
    builder.subject.contains("Newsletter", True)

    msgsColl = client.list_messages(builder.get_query())

    print("Filtered Messages Count: " + str(len(msgsColl)))
    #ExEnd: FilterMessagesFromMailbox

if __name__ == '__main__':
    run()
