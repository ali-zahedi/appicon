import json
import os
import shutil

from appicon.icongen import BaseIconGen


class IOSIconGen(BaseIconGen):
    directory_name = 'ios/AppIcon.appiconset'

    def get_infos(self) -> list:
        data = []
        with open(self.content_json_path) as json_file:
            dt = json.load(json_file)
            data = list(
                map(
                    lambda x: {'size': x.get('size', None), 'filename': x.get('filename', None)},
                    dt.get('images', [])
                )
            )
        return data

    @property
    def content_json_path(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(base_dir, 'Contents.json')

    def copy_other_items(self):
        shutil.copy(self.content_json_path, self.get_directory())
