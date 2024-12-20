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
                
Input = one_of(
    integers(),
    floats(),
    booleans(),
    text(),
    lists(integers()),
    tuples(integers()),
    lists(lists(integers())),
    tuples(tuples(integers()))
)

strategy = Input
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def find_lists(Input): 
	if isinstance(Input, list): 
		return 1
	else: 
		return len(Input) 

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, find_lists, *args)
