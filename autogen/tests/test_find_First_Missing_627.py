import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
array = lists(integers(min_value=1, max_value=sys.maxsize), unique=True, ordered=True)
start = integers(min_value=0, max_value=len(array)-1)
end = integers(min_value=0, max_value=len(array)-1)

strategy = array, start, end
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
def test_fuzz(args):
    run_with_timeout(0.3, find_First_Missing, *args)
