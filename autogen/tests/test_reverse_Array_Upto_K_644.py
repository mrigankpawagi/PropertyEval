import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
input_array = lists(integers(), min_size=1)
k = integers(min_value=0, max_value=MAX_SEQUENCE_LEN)

strategy = input_array, k
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def reverse_Array_Upto_K(input, k): 
  return (input[k-1::-1] + input[k:]) 

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, reverse_Array_Upto_K, *args)
