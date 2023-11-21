import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
num = integers(min_value=2, max_value=MAX_INT)

strategy = num
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def prime_num(num):
  if num >=1:
   for i in range(2, num//2):
     if (num % i) == 0:
                return False
     else:
                return True
  else:
          return False

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, prime_num, *args)
