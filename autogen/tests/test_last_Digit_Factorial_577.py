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

def last_Digit_Factorial(n): 
    if (n == 0): return 1
    elif (n <= 2): return n  
    elif (n == 3): return 6
    elif (n == 4): return 4 
    else: 
      return 0

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, last_Digit_Factorial, *args)
