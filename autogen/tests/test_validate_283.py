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
                
from hypothesis.strategies import decimals

n = decimals(min_value=0, max_value=10**MAX_SEQUENCE_LEN)
strategy = n
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def validate(n): 
    for i in range(10): 
        temp = n;  
        count = 0; 
        while (temp): 
            if (temp % 10 == i): 
                count+=1;  
            if (count > i): 
                return False
            temp //= 10; 
    return True

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, validate, *args)
