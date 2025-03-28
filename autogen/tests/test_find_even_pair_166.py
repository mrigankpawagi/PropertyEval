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
                
A = lists(integers(min_value=0, max_value=MAX_INT), min_size=2, max_size=MAX_SEQUENCE_LEN)
strategy = A
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def find_even_pair(A): 
  count = 0
  for i in range(0, len(A)): 
    for j in range(i+1, len(A)): 
        if ((A[i] ^ A[j]) % 2 == 0): 
          count += 1

  return count

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, find_even_pair, *args)
