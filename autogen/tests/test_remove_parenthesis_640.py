import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
items_without_parenthesis = text(alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', max_size=MAX_SEQUENCE_LEN).filter(lambda x: len(x) < MAX_SEQUENCE_LEN)
strategy = items_without_parenthesis
if not isinstance(strategy, tuple):
    strategy = (strategy,)

import re
def remove_parenthesis(items):
 for item in items:
    return (re.sub(r" ?\([^)]+\)", "", item))

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, remove_parenthesis, *args)
