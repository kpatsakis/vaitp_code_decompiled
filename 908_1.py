# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 908_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 667 bytes
import tensorflow as tf

def draw_bounding_boxes(boxes, image, colors):
    return tf.raw_ops.DrawBoundingBoxesV2(boxes=boxes, image=image, colors=colors)


boxes = tf.constant([[0.1, 0.2, 0.5, 0.5], [0.3, 0.3]], dtype=(tf.float32))
image = tf.zeros([100, 100, 3], dtype=(tf.float32))
colors = tf.constant([[1.0, 0.0, 0.0]], dtype=(tf.float32))
output_image = draw_bounding_boxes(boxes, image, colors)

# okay decompiling 908_1.pyc
