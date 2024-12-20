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
                
n = integers(min_value=0, max_value=56)
strategy = n
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def bell_number(n):   
    bell = [[0 for i in range(n+1)] for j in range(n+1)] 
    bell[0][0] = 1
    for i in range(1, n+1): 
        bell[i][0] = bell[i-1][i-1]  
        for j in range(1, i+1): 
            bell[i][j] = bell[i-1][j-1] + bell[i][j-1]   
    return bell[n][0] 

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, bell_number, *args)
