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
                
list1 = lists(integers(), min_size=1, max_size=MAX_SEQUENCE_LEN)
m = integers(min_value=0)
n = integers(min_value=0)

strategy = list1, m, n
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def sum_range_list(list1, m, n):                                                                                                                                                                                                
    sum_range = 0                                                                                                                                                                                                         
    for i in range(m, n+1, 1):                                                                                                                                                                                        
        sum_range += list1[i]                                                                                                                                                                                                  
    return sum_range   

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, sum_range_list, *args)
