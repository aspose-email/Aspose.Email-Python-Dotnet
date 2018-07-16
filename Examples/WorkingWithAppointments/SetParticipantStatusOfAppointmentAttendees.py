import aspose.email as ae
import datetime as dt
from aspose.email.calendar import Appointment

def run():
    #ExStart: SetParticipantStatusOfAppointmentAttendees
    location = "Room 5"
    startDate = dt.datetime(2011, 12, 10, 10, 12, 11)
    endDate = dt.date(2012, 11, 13)
    organizer = ae.MailAddress("aaa@amail.com", "Organizer")
    attendees = ae.MailAddressCollection()
    attendee1 = ae.MailAddress("bbb@bmail.com", "First attendee")
    attendee2 = ae.MailAddress("ccc@cmail.com", "Second attendee")
    attendee1.participation_status = ae.ParticipationStatus.ACCEPTED
    attendee2.participation_status = ae.ParticipationStatus.DECLINED
    attendees.append(attendee1)
    attendees.append(attendee2)
    target2 = Appointment(location, startDate, endDate, organizer, attendees)
    #ExEnd: SetParticipantStatusOfAppointmentAttendees

if __name__ == '__main__':
    run()
