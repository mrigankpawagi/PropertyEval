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
                
numbers = lists(integers(), unique=True, min_size=2)
strategy = numbers
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def second_smallest(numbers):
  unique_numbers = list(set(numbers))
  unique_numbers.sort()
  if len(unique_numbers) < 2:
    return None
  else:
    return unique_numbers[1]

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, second_smallest, *args)
