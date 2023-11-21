import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
@composite
def create_dict(draw):
    keys = draw(lists(text(alphabet=string.ascii_letters, min_size=1, max_size=10), min_size=1, max_size=5))
    def recur_dict():
        values = draw(lists(one_of(integers(), text()), min_size=1, max_size=5))
        return dict(zip(keys, values))
    return draw(recursive(none() | recur_dict, dict))

d = create_dict()

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
