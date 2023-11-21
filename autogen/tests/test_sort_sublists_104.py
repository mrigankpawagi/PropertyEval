import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
input_list = lists(lists(text(alphabet=characters(whitespace=True), min_size=1), min_size=1), min_size=1)

strategy = input_list
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def sort_sublists(input_list):
    result = [sorted(x, key = lambda x:x[0]) for x in input_list] 
    return result


@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, sort_sublists, *args)
