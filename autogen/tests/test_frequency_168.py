import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
a = lists(integers(min_value=MIN_INT, max_value=MAX_INT), min_size=SMALL_SEQUENCE_LEN, max_size=MAX_SEQUENCE_LEN)
x = integers(min_value=MIN_INT, max_value=MAX_INT)

strategy = a, x
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def frequency(a,x): 
    count = 0  
    for i in a: 
      if i == x: 
        count += 1

    return count 

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, frequency, *args)
