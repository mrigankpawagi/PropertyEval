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
                
input_list = lists(lists(integers()), max_size=MAX_SEQUENCE_LEN)
strategy = input_list
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def count_list(input_list): 
    return len(input_list)

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, count_list, *args)
