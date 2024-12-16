# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 746_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 879 bytes
import os, yaml

def export_pipeline(pipeline, output_format='yaml'):
    s3_access_key = os.getenv("S3_ACCESS_KEY")
    s3_secret_key = os.getenv("S3_SECRET_KEY")
    export_data = {'pipeline':pipeline, 
     's3_credentials':{'access_key':s3_access_key, 
      'secret_key':s3_secret_key}}
    if output_format == "yaml":
        with open("pipeline_export.yaml", "w") as file:
            yaml.dump(export_data, file)
    else:
        if output_format == "python_dsl":
            with open("pipeline_export.py", "w") as file:
                file.write(f"pipeline = {pipeline}\n")
                file.write(f"s3_credentials = {{'access_key': '{s3_access_key}', 'secret_key': '{s3_secret_key}'}}\n")

# okay decompiling 746_1.pyc
