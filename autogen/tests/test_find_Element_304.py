import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
arr = lists(integers(), min_size=1)
ranges = lists(lists(integers(min_value=0), min_size=2, max_size=2), min_size=1)
rotations = integers(min_value=0)
index = integers(min_value=0)

strategy = arr, ranges, rotations, index
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def find_Element(arr,ranges,rotations,index) :  
    for i in range(rotations - 1,-1,-1 ) : 
        left = ranges[i][0] 
        right = ranges[i][1] 
        if (left <= index and right >= index) : 
            if (index == left) : 
                index = right 
            else : 
                index = index - 1 
    return arr[index] 

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, find_Element, *args)
