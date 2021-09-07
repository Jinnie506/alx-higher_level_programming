#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    rem = number % (-10)
else:
    rem = number % 10
if rem > 5:
    print("Last digit of {:d} is {:d} and is greater than five"
          .format(number, rem))
elif rem is 0:
    print("Last digit of {} is {} and is zero".format(number, rem))
else:
    print("Last digit of {} is {} and is less than 6 and not 0"
          .format(number, rem))
 
