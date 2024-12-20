import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given, settings
from timeout import run_with_timeout
from typing import *
                
dict = dictionaries(text(), text(), min_size=1, max_size=10)
n = text()
strategy = dict, n
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def check_value(dict, n):
    result = all(x == n for x in dict.values()) 
    return result

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, check_value, *args)
