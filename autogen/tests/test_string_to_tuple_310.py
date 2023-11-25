import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
str1 = text(alphabet="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", min_size=1, max_size=1)
strategy = str1.map(lambda s: (s,))
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def string_to_tuple(str1):
    result = tuple(x for x in str1 if not x.isspace()) 
    return result

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, string_to_tuple, *args)
