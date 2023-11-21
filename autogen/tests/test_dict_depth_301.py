import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
@composite
def nested_dict(draw):
    key = draw(text())
    value = recursive(base, dictionaries)
    return {key: value}

d = nested_dict()

strategy = d
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def dict_depth(d):
    if isinstance(d, dict):
        return 1 + (max(map(dict_depth, d.values())) if d else 0)
    return 0

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, dict_depth, *args)
