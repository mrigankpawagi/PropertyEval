import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
n = positive_integers()

strategy = n
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def divisor(n):
  for i in range(n):
    x = len([i for i in range(1,n+1) if not n % i])
  return x

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, divisor, *args)
