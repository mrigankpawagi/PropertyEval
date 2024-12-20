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
                
num1 = integers(min_value=2, max_value=1000000)
num2 = integers(min_value=2, max_value=1000000)

strategy = num1, num2
if not isinstance(strategy, tuple):
    strategy = (strategy,)

import math 
def div_sum(n): 
  total = 1
  i = 2

  while i * i <= n:
    if (n % i == 0):
      total = (total + i + math.floor(n / i))
    i += 1

  return total

def are_equivalent(num1, num2): 
    return div_sum(num1) == div_sum(num2); 

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, are_equivalent, *args)
