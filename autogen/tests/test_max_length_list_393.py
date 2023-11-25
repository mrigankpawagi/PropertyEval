import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
input_list = lists(elements=lists(booleans()), min_size=1, max_size=10)
strategy = input_list
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def max_length_list(input_list):
    max_length = max(len(x) for x in input_list )   
    max_list = max(input_list, key = lambda i: len(i))    
    return(max_length, max_list)

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, max_length_list, *args)
