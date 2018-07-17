from aspose.email import MailMessage
from aspose.email.storage.pst import *
from aspose.email.mime import HeaderCollection
import aspose.email.mapi.msg as msg 
from aspose.email.mapi import MapiTask, MapiProperty, TaskSaveFormat, MapiTaskHistory
from aspose.email.mapi import MapiTaskOwnership, MapiTaskStatus
import datetime as dt

def run():
	dataDir = "Data/"
	#ExStart: CreatingAndSavingOutlookTask
	task = MapiTask("To Do", "Just click and type to add new task", dt.datetime(2018, 6, 1, 21, 30, 0), dt.datetime(2018, 6, 4, 21, 30, 0))
	task.percent_complete = 20
	task.estimated_effort = 2000
	task.actual_effort = 20
	task.history = MapiTaskHistory.ASSIGNED
	task.last_update = dt.datetime(2018, 6, 1, 21, 30, 0)
	task.users.owner = "Darius"
	task.users.last_assigner = "Harkness"
	task.users.last_delegate = "Harkness"
	task.users.ownership = MapiTaskOwnership.ASSIGNERS_COPY
	task.companies = [ "company1", "company2", "company3" ]
	task.categories = [ "category1", "category2", "category3" ]
	task.mileage = "Some test mileage"
	task.billing = "Test billing information"
	task.users.delegator = "Test Delegator"
	task.sensitivity = MapiSensitivity.PERSONAL
	task.status = MapiTaskStatus.COMPLETE
	task.estimated_effort = 5
	task.save(dataDir + "CreatingAndSavingOutlookTask_out.msg", TaskSaveFormat.MSG)
	#ExEnd: CreatingAndSavingOutlookTask
	
if __name__ == '__main__':
    run()
