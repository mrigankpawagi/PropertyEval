import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given, settings
from timeout import run_with_timeout
from typing import *
                
array = lists(integers(min_value=1, max_value=MAX_INT), unique=True).map(lambda x: sorted(x))

strategy = array
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def find_First_Missing(array,start=0,end=None):
    if end is None:
      end = len(array) - 1   
    if (start > end): 
        return end + 1
    if (start != array[start]): 
        return start; 
    mid = int((start + end) / 2) 
    if (array[mid] == mid): 
        return find_First_Missing(array,mid+1,end) 
    return find_First_Missing(array,start,mid) 

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, find_First_Missing, *args)
