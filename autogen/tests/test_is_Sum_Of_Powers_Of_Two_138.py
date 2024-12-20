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
                
n = integers(min_value=0, max_value=1000000)
strategy = n
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def is_Sum_Of_Powers_Of_Two(n): 
    if (n % 2 == 1): 
        return False
    else: 
        return True

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, is_Sum_Of_Powers_Of_Two, *args)
