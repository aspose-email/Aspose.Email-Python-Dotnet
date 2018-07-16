from aspose.email.storage.pst import *
from aspose.email.mime import HeaderCollection
import aspose.email.mapi.msg as msg 
from aspose.email.mapi import MapiTask, MapiProperty, TaskSaveFormat, MapiTaskHistory
from aspose.email.mapi import MapiTaskOwnership, MapiTaskStatus, MapiTaskState, MapiCalendarWeeklyRecurrencePattern, MapiCalendarRecurrenceEndType
from aspose.email.mapi import MapiCalendarDailyRecurrencePattern, MapiCalendarRecurrencePatternType, MapiCalendarDayOfWeek, MapiCalendarMonthlyRecurrencePattern
import datetime as dt

def run():
	dataDir = ""
	#ExStart: AddRecurrenceToMapiTask
	startDate = dt.datetime(2015, 4, 30, 10, 00, 00)
	task = MapiTask("abc", "def", startDate, dt.datetime(2015, 4, 30, 11, 00, 00))
	task.state = MapiTaskState.NOT_ASSIGNED

	# Set the weekly recurrence
	rec = MapiCalendarDailyRecurrencePattern()
	rec.pattern_type = MapiCalendarRecurrencePatternType.DAY
	rec.period = 1
	rec.week_start_day = 0 #0 is for Sunday and so on. WeekStartDay=0
	rec.occurrence_count = 0
	task.recurrence = True
	task.save(dataDir + "AsposeDaily_out.msg", TaskSaveFormat.MSG)

	# Set the weekly recurrence
	rec1 = MapiCalendarWeeklyRecurrencePattern()
	rec1.pattern_type = MapiCalendarRecurrencePatternType.WEEK
	rec1.period = 1
	rec1.day_of_week = MapiCalendarDayOfWeek.WEDNESDAY
	rec1.end_type = MapiCalendarRecurrenceEndType.NEVER_END
	rec1.occurrence_count = 0
	task.recurrence = rec1
	task.save(dataDir + "AsposeWeekly_out.msg", TaskSaveFormat.MSG);

	# Set the monthly recurrence
	recMonthly =  MapiCalendarMonthlyRecurrencePattern()
	recMonthly.pattern_type = MapiCalendarRecurrencePatternType.MONTH
	recMonthly.period = 1
	recMonthly.end_type = MapiCalendarRecurrenceEndType.NEVER_END
	recMonthly.day = 30
	recMonthly.occurrence_count = 0 
	recMonthly.week_start_day = 0 #0 is for Sunday and so on. WeekStartDay=0
	task.recurrence = recMonthly
	task.save(dataDir + "AsposeMonthly_out.msg", TaskSaveFormat.MSG);

	# Set the yearly recurrence
	recYearly = MapiCalendarMonthlyRecurrencePattern()
	recYearly.pattern_type = MapiCalendarRecurrencePatternType.MONTH
	recYearly.end_type = MapiCalendarRecurrenceEndType.NEVER_END
	recYearly.occurrence_count = 10
	recYearly.period = 12
	task.recurrence = recYearly
	task.save(dataDir + "AsposeYearly_out.msg", TaskSaveFormat.MSG)
	#ExEnd: AddRecurrenceToMapiTask
	
if __name__ == '__main__':
    run()	