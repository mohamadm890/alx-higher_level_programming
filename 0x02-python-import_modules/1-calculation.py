#!/usr/bin/python3
import calculator_1
a = 10
b = 5
addfunction = calculator_1.add(a, b)
subfunction = calculator_1.sub(a, b)
mulfunction = calculator_1.mul(a, b)
divfunction = calculator_1.div(a, b)
print(f"{a} + {b} = {addfunction}")
print(f"{a} - {b} = {subfunction}")
print(f"{a} * {b} = {mulfunction}")
print(f"{a} / {b} = {divfunction}")
