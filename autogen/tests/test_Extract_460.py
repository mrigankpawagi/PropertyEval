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
                
lst = lists(lists(integers(), min_size=1), max_size=MAX_SEQUENCE_LEN)
strategy = lst
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def Extract(lst): 
    return [item[0] for item in lst] 

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, Extract, *args)
