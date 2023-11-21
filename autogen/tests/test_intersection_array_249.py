import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
array1 = lists(integers(), unique=True)
array2 = lists(integers(), unique=True)

strategy = array1, array2
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def intersection_array(array_nums1,array_nums2):
 result = list(filter(lambda x: x in array_nums1, array_nums2)) 
 return result

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, intersection_array, *args)
