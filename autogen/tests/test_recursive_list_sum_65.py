import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
def recursive_list():
    base = integers()
    return recursive(base, lists)

data_list = recursive_list()

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
