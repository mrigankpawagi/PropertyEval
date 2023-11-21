import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
n = integers(min_value=0, max_value=100)

strategy = n
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def find_Average_Of_Cube(n):  
    sum = 0
    for i in range(1, n + 1): 
        sum += i * i * i  
    return round(sum / n, 6) 

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, find_Average_Of_Cube, *args)
