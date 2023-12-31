import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
items = lists(text(alphabet='abc()', max_size=MAX_SEQUENCE_LEN), max_size=MAX_SEQUENCE_LEN)
strategy = items
if not isinstance(strategy, tuple):
    strategy = (strategy,)

import re
def remove_parenthesis(items):
 for item in items:
    return (re.sub(r" ?\([^)]+\)", "", item))

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, remove_parenthesis, *args)
