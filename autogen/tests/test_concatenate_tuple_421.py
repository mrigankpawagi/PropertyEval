import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
test_tup = lists(integers() | floats() | text() | booleans(), max_size=MAX_SEQUENCE_LEN).map(tuple)

strategy = test_tup
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def concatenate_tuple(test_tup):
    delim = "-"
    res = ''.join([str(ele) + delim for ele in test_tup])
    res = res[ : len(res) - len(delim)]
    return (str(res)) 

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, concatenate_tuple, *args)
