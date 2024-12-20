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
                
S = lists(elements=one_of(text(), integers()), max_size=MAX_SEQUENCE_LEN)
step = integers(min_value=1, max_value=MAX_SEQUENCE_LEN)

strategy = S, step
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def list_split(S, step):
    return [S[i::step] for i in range(step)]

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, list_split, *args)
