from aspose.email.clients.smtp import SmtpClient
from aspose.email.clients import SecurityOptions

#ExStart: SSLEnabledSMTPServer
client = SmtpClient()
client.host = "smtp.gmail.com"
client.port = 587
client.username = "username"
client.password = "password"
client.security_options = SecurityOptions.SSLEXPLICIT
#ExEnd: SSLEnabledSMTPServer
