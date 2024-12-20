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
                
from typing import Any, List

@composite
def nested_list(draw, elements_strategy):
    base = elements_strategy | lists(nested_list(elements_strategy), max_size=MAX_SEQUENCE_LEN)
    return draw(base)

def strategy_list_sum():
    strategy_elements = one_of(integers(), floats())
    return nested_list(strategy_elements)

strategy = strategy_list_sum()
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
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, recursive_list_sum, *args)
