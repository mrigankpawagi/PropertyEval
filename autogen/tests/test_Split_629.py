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
                
list_ = lists(integers(), max_size=MAX_SEQUENCE_LEN)
strategy = list_
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def Split(list): 
    return [num for num in list if num % 2 == 0]

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, Split, *args)
