import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
dictionary = dictionaries(keys=text(), values=integers(), min_size=1, max_size=10)
n = integers(min_value=MIN_INT, max_value=MAX_INT)

strategy = dictionary, n
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def check_value(dict, n):
    result = all(x == n for x in dict.values()) 
    return result

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, check_value, *args)
