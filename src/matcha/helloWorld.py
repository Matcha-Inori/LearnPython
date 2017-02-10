# coding = UTF-8
import sys
import os
import importlib

import matcha.package1.package1_1.script1_1 as script1_1

print('hello world')
print(sys.platform)
print(os.cpu_count())

script1_1.function_1_1('key1_1', 'value1_1')
print(script1_1.value_1_1)
script1_1.value_1_1 += 100
print(script1_1.value_1_1)
print(id(script1_1))

importlib.reload(script1_1)

print(id(script1_1))
print(script1_1.value_1_1)

print(dir(script1_1))
