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
                
input = lists(integers(), max_size=MAX_SEQUENCE_LEN)
k = integers(min_value=1, max_value=MAX_SEQUENCE_LEN)

strategy = input, k
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def reverse_Array_Upto_K(input, k): 
  return (input[k-1::-1] + input[k:]) 

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, reverse_Array_Upto_K, *args)
