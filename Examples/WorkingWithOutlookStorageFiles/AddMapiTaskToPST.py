from aspose.email.storage.pst import *
from aspose.email.mapi import MapiTask
from aspose.email.mapi import MapiTaskOwnership
from aspose.email.mapi import MapiTaskHistory
import datetime as dt
from datetime import timedelta

def run():
	dataDir = "Data/"
	#ExStart: AddMapiTaskToPST
	task = MapiTask("To Do", "Just click and type to add new task", dt.datetime.now(), dt.datetime.today() + timedelta(days=3))
	task.percent_complete = 20
	task.estimated_effort = 2000
	task.actual_effort = 20
	task.history = MapiTaskHistory.ASSIGNED
	task.last_update = dt.datetime.now()
	task.users.owner = "Darius"
	task.users.last_assigner = "Harkness"
	task.users.last_delegate = "Harkness";
	task.users.ownership = MapiTaskOwnership.ASSIGNERS_COPY

	personalStorage = PersonalStorage.create(dataDir + "AddMapiTaskToPST_out.pst", FileFormatVersion.UNICODE)

	tasksFolder = personalStorage.create_predefined_folder("Tasks", StandardIpmFolder.TASKS)
	tasksFolder.add_mapi_message_item(task)

	personalStorage.dispose()
	#ExEnd: AddMapiTaskToPST

if __name__ == '__main__':
    run()	
