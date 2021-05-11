from .ios import IOSIconGen
from .android import AndroidIconGen


def icon_generate(logo_path, destination_directory):
    ios = IOSIconGen(logo_path, destination_directory)
    android = AndroidIconGen(logo_path, destination_directory)
    for i in [ios, android]:
        i.create()


def to_zip(source_directory, destination_path, is_remove_source_directory=False):
    import os
    import shutil
    import zipfile
    def zipdir(path, ziph):
        # ziph is zipfile handle
        for root, dirs, files in os.walk(path):
            for file in files:
                ziph.write(os.path.join(root, file),
                           os.path.relpath(os.path.join(root, file),
                                           os.path.join(path, '..')))

    zipf = zipfile.ZipFile(destination_path, 'w', zipfile.ZIP_DEFLATED)
    zipdir(source_directory, zipf)
    zipf.close()
    if is_remove_source_directory:
        shutil.rmtree(source_directory)
