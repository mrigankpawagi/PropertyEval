import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
S = lists(elements=anything())
step = integers(min_value=1, max_value=MAX_SEQUENCE_LEN)

strategy = S, step
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def list_split(S, step):
    return [S[i::step] for i in range(step)]

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, list_split, *args)
