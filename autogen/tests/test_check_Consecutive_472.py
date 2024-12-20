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
                
l = lists(integers(), min_size=1, unique=True)
strategy = l
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def check_Consecutive(l): 
    return sorted(l) == list(range(min(l),max(l)+1)) 

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, check_Consecutive, *args)
