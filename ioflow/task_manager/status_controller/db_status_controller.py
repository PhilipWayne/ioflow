import time

import requests

from ioflow.task_manager.status_controller.status_controller_base import \
    StatusControllerBase


class DbStatusController(StatusControllerBase):
    def __init__(self, config, *args, **kwargs):
        self.config = config
        self.time_interval = config.get('db_status_check_interval', 10)

        self.code_mapping = {
            "suspend": self.PAUSE,
            "continue": self.CONTINUE,
            "stop": self.STOP
        }

        super().__init__(*args, **kwargs)

    def main(self, pause_event, stop_event):
        last_check_timestamp = time.time()

        while True:
            # only check if time longer than time interval
            if last_check_timestamp + self.time_interval < time.time():
                time.sleep(self.time_interval / 10)

            last_check_timestamp = time.time()

            cmd = self.get_cmd()

            self.exec(cmd, pause_event, stop_event)

    def get_cmd(self):
        r = requests.get(self.config['task_info_url'], params={'taskId': self.config['task_id']})
        data = r.json()

        operation = data['data']['operation']

        return self.code_mapping[operation]
