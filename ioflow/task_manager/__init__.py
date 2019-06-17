from ioflow.task_manager.local_task_manager import LocalTaskManager
from ioflow.task_manager.db_task_manager import DbTaskManager

task_manager_class_registry = {}


def get_performance_metrics_class(config):
    return task_manager_class_registry[config.get('task_manager_schema', 'local')]


def registry_performance_metrics_class(schema, class_):
    task_manager_class_registry[schema] = class_


registry_performance_metrics_class('local', LocalTaskManager)
registry_performance_metrics_class('db', DbTaskManager)
