import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
A = lists(integers(min_value=MIN_INT, max_value=MAX_INT), min_size=SMALL_SEQUENCE_LEN, max_size=MAX_SEQUENCE_LEN)
B = lists(integers(min_value=MIN_INT, max_value=MAX_INT), min_size=SMALL_SEQUENCE_LEN, max_size=MAX_SEQUENCE_LEN)

strategy = A, B
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def is_Sub_Array(A,B): 
    n = len(A)
    m = len(B)
    i = 0; j = 0; 
    while (i < n and j < m):  
        if (A[i] == B[j]): 
            i += 1; 
            j += 1; 
            if (j == m): 
                return True;  
        else: 
            i = i - j + 1; 
            j = 0;       
    return False; 

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, is_Sub_Array, *args)
