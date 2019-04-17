from ioflow.task_manager.task_manager import TaskManager
from ioflow.task_manager.status_controller.local_status_controller import local_status_controller


class LocalTaskManager(TaskManager):
    def __init__(self):
        super(LocalTaskManager, self).__init__(local_status_controller)
