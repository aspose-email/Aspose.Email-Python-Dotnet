from datetime import datetime, timedelta, tzinfo
from calendar import timegm
from tempfile import TemporaryDirectory
from aspose.email.mapi import MapiPropertyTag, MapiMessage, MapiProperty, MapiMessageFlags

#ExStart: ConvertDateTime
def long_to_mapi_bytes(x):
    return x.to_bytes(8, 'little')

# http://support.microsoft.com/kb/167296
# How To Convert a UNIX time_t to a Win32 FILETIME or SYSTEMTIME
EPOCH_AS_FILETIME = 116444736000000000  # January 1, 1970 as MS file time
HUNDREDS_OF_NANOSECONDS = 10000000

class FakeUTC(tzinfo):
    def utcoffset(self, dt):
        return timedelta(0)

    def tzname(self, dt):
        return "UTC"

    def dst(self, dt):
        return timedelta(0)

utc = FakeUTC()

def dt_to_filetime(dt):
    if (dt.tzinfo is None) or (dt.tzinfo.utcoffset(dt) is None):
        dt = dt.replace(tzinfo=utc)
    ft = EPOCH_AS_FILETIME + (timegm(dt.timetuple()) * HUNDREDS_OF_NANOSECONDS)
    return ft + (dt.microsecond * 10)

def date_to_mapi_bytes(dt):
    ft = dt_to_filetime(dt)
    return long_to_mapi_bytes(ft)
#ExEnd: ConvertDateTime
def run():

    dataDir = "Data/"
    #ExStart: SetMapiProperties
    # Setting MAPI Properties sample
    msg = MapiMessage("user1@gmail.com", "user2@gmail.com", "This is subject", "This is body")
    msg.set_property(MapiProperty(MapiPropertyTag.SENDER_ADDRTYPE, bytes("EX", "utf-8")))

    recipientTo = msg.recipients[0]
    propAddressType = MapiProperty(MapiPropertyTag.RECEIVED_BY_ADDRTYPE, bytes("MYFAX", "utf-8"))
    recipientTo.set_property(propAddressType);

    faxAddress = "My Fax User@/FN=fax#/VN=voice#/CO=My Company/CI=Local"
    propEmailAddress = MapiProperty(MapiPropertyTag.RECEIVED_BY_EMAIL_ADDRESS, bytes(faxAddress, "utf-8"))

    recipientTo.set_property(propEmailAddress)

    msg.set_message_flags(MapiMessageFlags.UNSENT | MapiMessageFlags.FROMME)
    msg.set_property( MapiProperty(MapiPropertyTag.RTF_IN_SYNC, long_to_mapi_bytes(1)) )

    # DateTime property
    modification_date = datetime(2013, 9, 11)
    prop = MapiProperty(MapiPropertyTag.LAST_MODIFICATION_TIME, date_to_mapi_bytes(modification_date))
    msg.set_property(prop)

    msg.save(dataDir + "SetMapiProperties_out.msg")
    #ExEnd: SetMapiProperties
