import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
A = lists(integers(min_value=MIN_INT, max_value=MAX_INT), max_size=N)
N = integers(min_value=1, max_value=MAX_SEQUENCE_LEN)

strategy = A, N
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def find_Odd_Pair(A,N) : 
    oddPair = 0
    for i in range(0,N) :  
        for j in range(i+1,N) :  
            if ((A[i] ^ A[j]) % 2 != 0):  
                oddPair+=1  
    return oddPair  

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, find_Odd_Pair, *args)
