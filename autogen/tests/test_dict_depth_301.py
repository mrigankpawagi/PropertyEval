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
                
d = fixed_dictionaries({"a": integers(), "b": fixed_dictionaries({"c": integers()})})
strategy = d
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def dict_depth(d):
    if isinstance(d, dict):
        return 1 + (max(map(dict_depth, d.values())) if d else 0)
    return 0

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, dict_depth, *args)
