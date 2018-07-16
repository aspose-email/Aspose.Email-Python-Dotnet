import aspose.email
from aspose.email.clients.imap import ImapClient
from aspose.email.clients import SecurityOptions
from aspose.email.clients.imap import ImapQueryBuilder
import datetime as dt
from datetime import timedelta
defrun():
    
    dataDir = ""

    try:
    #ExStart: GetMessagesWithSpecificCriterion    
                #Filter on Today's Date
                builder = ImapQueryBuilder()
                builder.internal_date.on(dt.datetime.now())

                #Filter messages on Date Range
                builder.internal_date.before(dt.datetime.now());
                builder.internal_date.since(dt.datetime.today() - timedelta(days=7))

                #Specific Sender
                builder.from_address.contains("saqib.razzaq@127.0.0.1")

                #Specific Domain
                builder.from_address.contains("SpecificHost.com")

                #Specific Recipient
                builder.to.contains("recipient");
    #ExEnd: GetMessagesWithSpecificCriterion
    except Exception as ex:
        print(str(ex))

if _name_ == '__main__':
    run()
