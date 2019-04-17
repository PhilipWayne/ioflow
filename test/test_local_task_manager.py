import sys

from ioflow.task_manager.local_task_manager import LocalTaskManager


def fake_client(task_manager):
    import time
    i = 0
    while i < 30:
        i += 1
        task_manager.wait()
        time.sleep(1)
        print("I am working pre 1s")
        if task_manager.should_stop():
            print("I am out")
            sys.exit(0)


task_manager = LocalTaskManager()

fake_client(task_manager)
