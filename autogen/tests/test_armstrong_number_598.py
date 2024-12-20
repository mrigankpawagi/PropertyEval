import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given, settings
from timeout import run_with_timeout
from typing import *
import math
import string
                
number = integers(min_value=0, max_value=MAX_INT)

strategy = number
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def armstrong_number(number):
 sum = 0
 times = 0
 temp = number
 while temp > 0:
           times = times + 1
           temp = temp // 10
 temp = number
 while temp > 0:
           reminder = temp % 10
           sum = sum + (reminder ** times)
           temp //= 10
 if number == sum:
           return True
 else:
           return False

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, armstrong_number, *args)
