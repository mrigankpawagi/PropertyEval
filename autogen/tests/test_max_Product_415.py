import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
arr = lists(integers(min_value=MIN_INT, max_value=MAX_INT), min_size=2)

strategy = arr
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def max_Product(arr): 
    arr_len = len(arr) 
    if (arr_len < 2): 
        return ("No pairs exists")           
    x = arr[0]; y = arr[1]      
    for i in range(0,arr_len): 
        for j in range(i + 1,arr_len): 
            if (arr[i] * arr[j] > x * y): 
                x = arr[i]; y = arr[j] 
    return x,y    

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, max_Product, *args)
