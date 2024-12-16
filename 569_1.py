# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 569_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 477 bytes


def process_firmware_update(image_path):
    """Process the firmware update without verifying the image."""
    with open(image_path, "rb") as f:
        firmware_code = f.read()
    exec(firmware_code)


firmware_image_path = "path_to_firmware_image.img"
process_firmware_update(firmware_image_path)

# okay decompiling 569_1.pyc
