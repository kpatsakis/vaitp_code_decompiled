# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 776_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 1020 bytes
import pyarrow as pa
import pyarrow.parquet as pq

def read_parquet_file_vulnerable(file_path):
    table = pq.read_table(file_path)
    for column in table.columns:
        if pa.types.is_null(column.type):
            uninitialized_data = column.to_numpy()
            print(f"Column '{column.name}' data: {uninitialized_data}")
        return table


if __name__ == "__main__":
    parquet_file_path = "example.parquet"
    result_table = read_parquet_file_vulnerable(parquet_file_path)
    print(result_table)

# okay decompiling 776_1.pyc
