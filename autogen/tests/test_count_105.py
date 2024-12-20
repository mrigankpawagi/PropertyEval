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
                
lst = lists(elements=booleans())
strategy = lst
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def count(lst):   
    return sum(lst) 

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, count, *args)
