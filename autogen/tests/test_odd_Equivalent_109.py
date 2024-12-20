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
                
s = text(alphabet='01', max_size=MAX_SEQUENCE_LEN)
n = integers(min_value=0, max_value=MAX_SEQUENCE_LEN)

strategy = s, n
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def odd_Equivalent(s,n): 
    count=0
    for i in range(0,n): 
        if (s[i] == '1'): 
            count = count + 1
    return count 

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, odd_Equivalent, *args)
