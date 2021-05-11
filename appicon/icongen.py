import abc
import os
import shutil
import tempfile

from PIL import Image

class BaseIconGen(metaclass=abc.ABCMeta):

    def __init__(self, logo_path, destination_path):
        if not os.path.exists(logo_path):
            raise FileNotFoundError("{0} file does not exist!".format(logo_path))
        self.logo_path = logo_path
        if not os.path.exists(destination_path):
            os.makedirs(destination_path)
        self.destination_path = destination_path

    @abc.abstractmethod
    def get_infos(self) -> list:
        """
        :return: [
            {
              "size": "20x20",
              "filename": "Icon-Small-60.png",
            }
        ]
        """
        pass

    @abc.abstractmethod
    def copy_other_items(self):
        raise NotImplementedError

    @property
    @abc.abstractmethod
    def directory_name(self) -> str:
        """

        :return: directory name like android or ios
        """
        raise NotImplementedError

    def get_directory(self):
        return os.path.join(self.destination_path, self.directory_name)

    def create(self):
        target_directory = self.get_directory()
        # sanitize dictionary
        infos = filter(lambda x: x.get('size', None) and x.get('filename', None), self.get_infos())
        with tempfile.TemporaryDirectory() as tmp_dirname:
            # resize
            img = Image.open(self.logo_path)
            for info in infos:
                filename = os.path.join(tmp_dirname, info['filename'])
                if not os.path.exists(os.path.dirname(filename)):
                    os.makedirs(os.path.dirname(filename))
                size = list(map(lambda x: int(float(x)), info['size'].split('x')))
                i = img.resize((size[0], size[1]), Image.ANTIALIAS)
                i.save(filename)
            # move to destination directory
            file_names = os.listdir(tmp_dirname)
            if not os.path.exists(target_directory):
                os.makedirs(target_directory)
            for file_name in file_names:
                shutil.move(os.path.join(tmp_dirname, file_name), target_directory)
        self.copy_other_items()
