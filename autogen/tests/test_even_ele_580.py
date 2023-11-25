import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
@composite
def create_mixed_tuple(draw):
    even_sublists = lists(integers(min_value=0, max_value=1000), min_size=1, max_size=10).filter(lambda lst: len(lst) % 2 == 0)
    odd_sublists = lists(integers(min_value=0, max_value=1000), min_size=1, max_size=10).filter(lambda lst: len(lst) % 2 != 0)
    sublist = one_of(even_sublists, odd_sublists)
    test_tuple = draw(tuples(sublist, sublist, sublist, sublist, sublist, sublist))
    return test_tuple

test_tuple = create_mixed_tuple()
even_fnc = integers(min_value=0, max_value=1000)

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
