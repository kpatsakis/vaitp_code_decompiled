# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 709_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 746 bytes
from pyspark import SparkConf, SparkContext
conf = SparkConf()
conf.set("spark.io.encryption.enabled", "true")
conf.set("spark.maxRemoteBlockSizeFetchToMem", "64m")
sc = SparkContext(conf=conf)
data = [
 1, 2, 3, 4, 5]
rdd = sc.parallelize(data)
broadcast_var = sc.broadcast(rdd.collect())

def multiply_by_two(x):
    return x * 2


result = rdd.map(multiply_by_two).collect()
print(result)
sc.stop()

# okay decompiling 709_1.pyc
