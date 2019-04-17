import functools
from threading import Event, Thread

from ioflow.task_manager.task_manager_base import TaskManagerBase


class TaskManager(TaskManagerBase):
    def __init__(self, status_controller_func):
        pause_event = Event()
        pause_event.set()

        stop_event = Event()
        stop_event.clear()  # just in case

        self.pause_event = pause_event
        self.stop_event = stop_event
        self.status_controller_func = status_controller_func

        t = Thread(target=functools.partial(self.status_controller_func, pause_event, stop_event))
        t.setDaemon(True)
        t.start()

    def should_stop(self) -> bool:
        """
        return True if task_manager is requested to stop task,
        otherwise will return false
        :return: bool
        """
        return self.stop_event.is_set()

    def wait(self):
        """
        this method will block if task_manager is requested to pause task,
        otherwise will return immediately, return value is not defined yet
        """
        self.pause_event.wait()
