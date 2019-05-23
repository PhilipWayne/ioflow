import os
import shutil
import tempfile

import requests

from ioflow.model_saver.model_saver_base import ModelSaverBase


class HttpBasedModelSaver(ModelSaverBase):
    def save_model(self, model_path):
        zipped_model = os.path.join(tempfile.mkdtemp(), 'model')
        model_zip_path = shutil.make_archive(zipped_model, 'zip', model_path)

        files = {
            'file': ('model.zip', open(model_zip_path, 'rb'), 'application/zip', {'Expires': '0'})
        }

        r = requests.post(self.config['data_url'],
                          json={'taskId': self.config['task_id']},
                          files=files)

        print(r.status_code)

        return model_zip_path
