import requests

task_status_registry = {}


def get_performance_metrics_class(config):
    return task_status_registry[config.get('performance_metrics_schema', 'raw')]


def registry_performance_metrics_class(schema, class_):
    task_status_registry[schema] = class_


class BasePerformanceMetrics(object):
    def __init__(self, config):
        self.config = config

    def set_metrics(self, metrics, global_step):
        raise NotImplementedError


class RawPerformanceMetrics(BasePerformanceMetrics):
    def __init__(self, config):
        super().__init__(config)

    def set_metrics(self, metrics, global_step):
        print('{}: {} => {}'.format(self.__class__, global_step, metrics))


registry_performance_metrics_class('raw', RawPerformanceMetrics)


class HttpPerformanceMetrics(BasePerformanceMetrics):
    def __init__(self, config):
        super().__init__(config)

    def set_metrics(self, metrics, global_step):
        json_data = {'id': self.config['task_id']}
        json_data.update({'step': {'date-time': None, 'global_step': global_step}, 'metrics': metrics})

        r = requests.post(self.config['metrics_report_url'], json=json_data)
        assert r.status_code == 200


registry_performance_metrics_class('http', HttpPerformanceMetrics)
