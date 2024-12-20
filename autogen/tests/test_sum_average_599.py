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
                
number = integers(min_value=1, max_value=MAX_SEQUENCE_LEN)
strategy = number
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def sum_average(number):
 total = 0
 for value in range(1, number + 1):
    total = total + value
 average = total / number
 return (total,average)

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, sum_average, *args)
