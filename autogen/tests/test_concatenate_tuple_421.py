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
                
test_tup = tuples(
    text(alphabet='abcdefghijklmnopqrstuvwxyz', min_size=1, max_size=1),
    integers(),
    text(alphabet='abcdefghijklmnopqrstuvwxyz', min_size=1, max_size=1),
    integers()
)
strategy = test_tup.map(lambda t: (concatenate_tuple(t),))
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def concatenate_tuple(test_tup):
    delim = "-"
    res = ''.join([str(ele) + delim for ele in test_tup])
    res = res[ : len(res) - len(delim)]
    return (str(res)) 

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, concatenate_tuple, *args)
