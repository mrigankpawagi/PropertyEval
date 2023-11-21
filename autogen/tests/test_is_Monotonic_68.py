import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
A = lists(integers(), min_size=1, max_size=MAX_SEQUENCE_LEN)

strategy = A
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def is_Monotonic(A): 
    return (all(A[i] <= A[i + 1] for i in range(len(A) - 1)) or
            all(A[i] >= A[i + 1] for i in range(len(A) - 1))) 

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, is_Monotonic, *args)
