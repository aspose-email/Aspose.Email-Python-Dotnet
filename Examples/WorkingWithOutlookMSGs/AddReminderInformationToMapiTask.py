from aspose.email.storage.pst import *
from aspose.email.mime import HeaderCollection
import aspose.email.mapi.msg as msg 
from aspose.email.mapi import MapiTask, MapiProperty, TaskSaveFormat, MapiTaskHistory
from aspose.email.mapi import MapiTaskOwnership, MapiTaskStatus
import datetime as dt

def run():
	dataDir = "Data/"
	#ExStart: AddReminderInformationToMapiTask
	task = MapiTask("To Do", "Just click and type to add new task", dt.datetime(2018, 6, 1, 21, 30, 0), dt.datetime(2018, 6, 4, 21, 30, 0))
	task.reminder_set = True
	task.reminder_time = dt.datetime(2018, 6, 1, 21, 30, 0)
	task.reminder_file_parameter =dataDir + "file://Alarm01.wav"
	task.save(dataDir + "AddReminderInformationToMapiTask_out.msg", TaskSaveFormat.MSG)
	#ExEnd: AddReminderInformationToMapiTask
	
if __name__ == '__main__':
    run()
