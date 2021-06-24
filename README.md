![GitHub](https://img.shields.io/github/license/aspose-email/Aspose.Email-Python-Dotnet)
# Aspose.Email for Python via .NET

[Aspose.Email for Python via .NET](https://products.aspose.com/email/python-net) is a complete set of Email Processing APIs to create, read and manipulate emails from within your Python applications. It makes it easier to work with many Outlook email message formats such as MSG, EML, EMLX and MHT files without the need of installing Microsoft Outlook. It also enables you to manage message storage files - Personal Storage Files (PST), Offline Storage Files (OST) along with message sending and receiving capabilities. You can also read and extract Outlook PST file that can be saved to disk in MSG format.

<p align="center">
<a title="Download complete Aspose.Email for Pytho via .NET source code" href="https://github.com/aspose-email/Aspose.Email-for-.NET/archive/master.zip">
	<img src="https://raw.github.com/AsposeExamples/java-examples-dashboard/master/images/downloadZip-Button-Large.png" />
  </a>
</p>

Directory | Description
--------- | -----------
[Examples](Examples)  | A collection of Python examples that help you learn the product features

## Email API Features

### General Email Features

- Create emails containing plain text as well as `HTML`.
- Create alternative message bodies.
- Connect to `SSL` enabled as well as `TLS` based SMTP server.

### Attachment Features

- Add/remove email attachments.
- Create attachments from file paths.

### Embedded Object Features

- Embed images, sound files or other types of objects into emails.
- Ability to embed objects from file paths, streams or byte arrays.

### Import/Export Features

- Import `MSG`, `MHT`, or `RFC822` compliant `EML` emails.
- Create emails from `HTML` content.
- Export emails to `MSG`, or `RFC822` compliant `EML` format.
- Export emails from an Outlook `PST` file to Outlook `MSG` files.

### Bulk Mail Features

- Send emails in batches.
- Built-in multi-threading feature for sending bulk emails.
- Save bulk email messages in a message pool.

### Calendar Features

- Add `iCalender` events to email messages.
- Cancel `iCalendar` events.
- Send meeting and appointment requests by email.

### Utility Features

- Customize email headers.
- Set message priority, date and time.
- Supports all character sets.
- Request read receipts.

### Advanced Features

- Asynchronous and synchronous programming models.
- Supports parsing emails in `MSG`, `MHT` and `EML` formats.
- Supports saving emails to `MSG`, `MHT` and `EML` formats.
- Extract attachments from Microsoft Outlook Email Message (`MSG`) files.
- Read messages from Outlook `PST` files.
- Supports backup `SMTP` connection.
- Specify the number of attempts for `SMTP` connections

For a more comprehensive list of features please visit [Features Overview](https://docs.aspose.com/email/pythonnet/features-overview/) page.

## Read & Write Email Formats

**Microsoft Outlook:** MSG, PST, OST, OFT\
**Email:** EML, EMLX, MBOX\
**Others:** ICS, VCF, HTML, MHTML

## Supported Environments

- **Microsoft Windows:** Windows Desktop & Server (`x86`, `x64`)
- **Python Versions:** Python `3.5` or higher

## Get Started with Aspose.Email for Python via .NET

Aspose.Email for Python via .NET is available as downloadable .whl file in the API’s download section as well as hosted on Pypi. For the detailed instructions please visit [Installing Aspose.Email for Python via .NET ](https://docs.aspose.com/email/pythonnet/installation/) documentation page.

## Filtering Messages from IMAP Mailbox
```php
For complete examples and data files, please go to https://github.com/aspose-email/aspose-email-python-dotnet
with ImapClient("imap.gmail.com", 993, "username", "password") as client:
        client.select_folder("Inbox")
        builder = ImapQueryBuilder()
        builder.subject.contains("Newsletter")
        builder.internal_date.on(dt.datetime.now())
        query = builder.get_query()
        msgsColl = client.list_messages(query)
        print("Total Messages fulfilling search criterion: " + str(len(msgsColl)))
```

[Home](https://www.aspose.com/) | [Product Page](https://products.aspose.com/email/python-net) | [Docs](https://docs.aspose.com/email/pythonnet/) | [Demos](https://products.aspose.app/email/family) | [API Reference](https://apireference.aspose.com/email/java) | [Examples](https://github.com/aspose-email/Aspose.Email-Python-Dotnet/tree/master/Examples) | [Blog](https://blog.aspose.com/category/email/) | [Search](https://search.aspose.com/) | [Free Support](https://forum.aspose.com/c/email) | [Temporary License](https://purchase.aspose.com/temporary-license)
