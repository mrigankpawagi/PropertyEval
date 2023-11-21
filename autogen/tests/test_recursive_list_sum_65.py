import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
@composite
def nested_list():
    elements = one_of(integers(), nested_lists())
    return lists(elements)

def recursive_list_sum(lst):
    if isinstance(lst, int):
        return lst
    else:
        return sum(recursive_list_sum(x) for x in lst)

data_list = nested_list()

strategy = data_list
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def recursive_list_sum(data_list):
	total = 0
	for element in data_list:
		if type(element) == type([]):
			total = total + recursive_list_sum(element)
		else:
			total = total + element
	return total

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, recursive_list_sum, *args)
