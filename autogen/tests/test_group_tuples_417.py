import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given, settings
from timeout import run_with_timeout
from typing import *
                
Input = lists(tuples(integers(), text()), min_size=1, max_size=MAX_SEQUENCE_LEN)
strategy = Input
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def group_tuples(Input): 
	out = {} 
	for elem in Input: 
		try: 
			out[elem[0]].extend(elem[1:]) 
		except KeyError: 
			out[elem[0]] = list(elem) 
	return [tuple(values) for values in out.values()] 

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, group_tuples, *args)
