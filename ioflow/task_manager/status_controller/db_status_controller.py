import time

from ioflow.task_manager.status_controller.status_controller_base import \
    StatusControllerBase


class DbStatusController(StatusControllerBase):
    def __init__(self, config, *args, **kwargs):
        self.config = config
        self.time_interval = config['db_status_check_interval']

        super().__init__(*args, **kwargs)

    def main(self, pause_event, stop_event):
        last_check_timestamp = time.time()

        while True:
            # only check if time longer than time interval
            if last_check_timestamp + self.time_interval < time.time():
                time.sleep(self.time_interval / 10)

            cmd = self.get_cmd()

            self.exec(cmd, pause_event, stop_event)

    def get_cmd(self):
        # TODO
        pass
