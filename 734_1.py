# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 734_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 502 bytes
import onnx

def load_onnx_model(model_path):
    model = onnx.load(model_path)
    for tensor in model.graph.initializer:
        if tensor.external_data:
            external_data_path = tensor.external_data
            print(f"Loading external data from: {external_data_path}")
        return model


model = load_onnx_model("model.onnx")

# okay decompiling 734_1.pyc
