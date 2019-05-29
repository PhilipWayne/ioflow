import requests


class TaskStatus(object):
    def __init__(self, config):
        self.config = config
        self.DONE = 10
        self.START = 1

    def send_status(self, status):
        print('{}:{}'.format(self.__class__, status))

        code_to_str = {
            self.DONE: 'done',
            self.START: 'start'
        }

        r = requests.post(self.config['progress_report_url'], json={'id': self.config['task_id'], 'progress': code_to_str[status]})
        assert r.status_code == 200


if __name__ == "__main__":
    config = {
        "progress_report_url": "http://10.43.13.8:25005/redis",
        "task_id": "121554"
    }

    ts = TaskStatus(config)
    ts.send_status(ts.START)
