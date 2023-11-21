import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
num = integers(min_value=MIN_INT, max_value=MAX_INT)

strategy = num
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def rev(num):    
    rev_num = 0
    while (num > 0):  
        rev_num = (rev_num * 10 + num % 10) 
        num = num // 10  
    return rev_num  
def check(n):    
    return (2 * rev(n) == n + 1)  

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, rev, *args)
