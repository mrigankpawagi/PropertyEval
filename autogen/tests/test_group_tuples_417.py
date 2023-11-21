import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
Input = lists(tuples(alpha(), alpha()), min_size=1)

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
def test_fuzz(args):
    run_with_timeout(0.3, group_tuples, *args)
