import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
@composite
def mixed_tuple(draw):
    elements = draw(lists(integers(), min_size=1))
    nested_tuples = draw(lists(mixed_tuple(), min_size=1))
    return tuple(elements + nested_tuples)

test_tuple = mixed_tuple()
even_fnc = from_type(bool)

strategy = test_tuple, even_fnc
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def even_ele(test_tuple, even_fnc): 
	res = tuple() 
	for ele in test_tuple: 
		if isinstance(ele, tuple): 
			res += (even_ele(ele, even_fnc), ) 
		elif even_fnc(ele): 
			res += (ele, ) 
	return res 
def extract_even(test_tuple):
  res = even_ele(test_tuple, lambda x: x % 2 == 0)
  return (res) 

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, even_ele, *args)
