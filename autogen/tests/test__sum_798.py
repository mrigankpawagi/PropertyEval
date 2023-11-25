import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
arr = lists(integers(), max_size=MAX_SEQUENCE_LEN)
strategy = arr
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def _sum(arr):  
    sum=0
    for i in arr: 
        sum = sum + i      
    return(sum)  

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, _sum, *args)
