import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
dict_keys = lists(text(min_size=1), min_size=1, unique=True)
dict_values = shared(integers())

d = dictionaries(keys=dict_keys, values=dict_values, min_size=1)

n = shared(dict_values)

strategy = d, n
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def check_value(dict, n):
    result = all(x == n for x in dict.values()) 
    return result

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, check_value, *args)
