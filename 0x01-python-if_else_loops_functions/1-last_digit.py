#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
Result = "Last digit of"
if last_digit > 5:
   print(f"{Result} {number} is {last_digit} and is greater than 5")
elif last_digit == 0:
   print(f"{Result} {number} is {last_digit} and is 0")
else:
   print(f"{Result} {number} is {last_digit} and is less than 6 and not 0")
