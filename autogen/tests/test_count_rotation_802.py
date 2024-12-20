import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given, settings
from timeout import run_with_timeout
from typing import *
                
from hypothesis import strategies as st

arr = st.lists(st.integers(), min_size=1)

strategy = arr
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def count_rotation(arr):   
    for i in range (1,len(arr)): 
        if (arr[i] < arr[i - 1]): 
            return i  
    return 0

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, count_rotation, *args)
