from .ios import IOSIconGen
from .android import AndroidIconGen


def icon_generate(logo_path, destination_path):
    ios = IOSIconGen(logo_path, destination_path)
    android = AndroidIconGen(logo_path, destination_path)
    for i in [ios, android]:
        i.create()
