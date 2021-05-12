from .ios import IOSIconGen
from .android import AndroidIconGen


def icon_generate(logo_path, destination_directory, is_zip=True):
    import os
    dd = destination_directory
    icon_set_name = 'icon_set'
    if is_zip:
        dd = os.path.join(dd, icon_set_name)
    ios = IOSIconGen(logo_path, dd)
    android = AndroidIconGen(logo_path, dd)
    for i in [ios, android]:
        i.create()
    if is_zip:
        dest = os.path.join(destination_directory, f'{icon_set_name}.zip')
        _to_zip(dd, dest, is_remove_source_directory=True)
        return dest
    return destination_directory


def _to_zip(source_directory, destination_path, is_remove_source_directory=False):
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
