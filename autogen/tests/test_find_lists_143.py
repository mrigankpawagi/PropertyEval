import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
Input = tuples(lists(integers()))

strategy = Input
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def find_lists(Input): 
	if isinstance(Input, list): 
		return 1
	else: 
		return len(Input) 

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, find_lists, *args)
