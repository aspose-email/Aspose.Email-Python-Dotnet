import aspose.email
from aspose.email.clients.imap import ImapClient
from aspose.email.clients import SecurityOptions
from aspose.email.clients.imap import ImapQueryBuilder
from aspose.email.clients.imap import ImapMessageFlags
import datetime as dt
from datetime import timedelta

def run():
	dataDir = ""

	try:
		#ExStart: BuildingComplexQueries
		#Combine Queries with And
		builder = ImapQueryBuilder("utf-8")
		builder.from_address.contains("SpecificHost.com")
				
		#Date Range
		builder.internal_date.before(dt.datetime.now())
		builder.internal_date.since(dt.datetime.today() - timedelta(days=7))

		#Combining Queries with OR
		builder.either(builder.subject.contains("test"), builder.from_address.contains("noreply@host.com"));

		#Filtering on Internal Date
		builder.internal_date.on(dt.datetime.now())

		#Case-Sensitive Email Filtering
		builder.subject.contains("Newsletter", True)
		builder.internal_date.on(dt.datetime.now())

		#GetMessagesWithCustomFlag
		builder.has_flags(ImapMessageFlags.keyword("custom1"))

		builder.has_no_flags(ImapMessageFlags.keyword("custom2"))
		#ExEnd: BuildingComplexQueries

	except Exception as ex:
		print(str(ex))

if __name__ == '__main__':
    run()
