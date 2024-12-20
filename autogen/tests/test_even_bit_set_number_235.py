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
                
n = integers(min_value=0, max_value=MAX_INT)
strategy = n
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def even_bit_set_number(n): 
    count = 0;res = 0;temp = n 
    while(temp > 0): 
        if (count % 2 == 1): 
            res |= (1 << count)
        count+=1
        temp >>= 1
    return (n | res) 

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, even_bit_set_number, *args)
