# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 966_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 773 bytes
import tensorflow as tf

def reverse_sequence(input_tensor, seq_lengths, batch_dim):
    input_rank = tf.rank(input_tensor)
    if batch_dim >= input_rank:
        raise ValueError("batch_dim exceeds the rank of the input tensor")
    return tf.reverse_sequence(input_tensor, seq_lengths, seq_axis=batch_dim)


input_tensor = tf.constant([[1, 2, 3], [4, 5, 6]])
seq_lengths = tf.constant([2, 3])
batch_dim = -1
output = reverse_sequence(input_tensor, seq_lengths, batch_dim)
print(output)

# okay decompiling 966_1.pyc
