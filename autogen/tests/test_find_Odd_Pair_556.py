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
                
A = lists(integers(min_value=0, max_value=MAX_INT), min_size=1, max_size=MAX_SEQUENCE_LEN)
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
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, find_Odd_Pair, *args)
