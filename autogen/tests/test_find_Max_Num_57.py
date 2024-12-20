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
                
arr = lists(integers(min_value=1, max_value=9), min_size=1, max_size=MAX_SEQUENCE_LEN)
strategy = arr
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def find_Max_Num(arr) : 
    n = len(arr)
    arr.sort(reverse = True) 
    num = arr[0] 
    for i in range(1,n) : 
        num = num * 10 + arr[i] 
    return num 

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, find_Max_Num, *args)
