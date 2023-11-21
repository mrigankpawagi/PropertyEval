import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
n = integers(min_value=0)

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
def test_fuzz(args):
    run_with_timeout(0.3, validate, *args)
