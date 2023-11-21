import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
names = lists(text(min_size=1), min_size=1, unique=True)
scores = lists(integers(min_value=0))
tuples = lists(tuples(names, scores), min_size=1)

strategy = tuples
if not isinstance(strategy, tuple):
    strategy = (strategy,)

from collections import defaultdict
def max_aggregate(stdata):
    temp = defaultdict(int)
    for name, marks in stdata:
        temp[name] += marks
    return max(temp.items(), key=lambda x: x[1])

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, max_aggregate, *args)
