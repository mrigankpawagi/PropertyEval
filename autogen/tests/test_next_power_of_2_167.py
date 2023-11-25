import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
n = integers(min_value=0, max_value=MAX_INT)
strategy = n
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def next_power_of_2(n): 
  if n and not n & (n - 1):
    return n

  count = 0
  while n != 0: 
    n >>= 1
    count += 1

  return 1 << count; 

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, next_power_of_2, *args)
