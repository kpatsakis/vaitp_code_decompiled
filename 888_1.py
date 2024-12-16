# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 888_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 601 bytes
import tensorflow as tf, numpy as np, tempfile
temp_file = tempfile.NamedTemporaryFile(delete=False)
data = np.random.rand(10).astype(np.float32)
data.tofile(temp_file.name)
tensor = tf.raw_ops.ImmutableConst(file=(temp_file.name), dtype=(tf.float32))
print(tensor)
temp_file.close()

# okay decompiling 888_1.pyc
