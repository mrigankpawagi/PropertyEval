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
                
items = lists(dictionaries(keys=text(alphabet='abcdefghijklmnopqrstuvwxyz', min_size=1, max_size=7), values=floats(min_value=0.0, exclude_min=True)), min_size=1, max_size=MAX_SEQUENCE_LEN)
n = integers(min_value=1, max_value=MAX_SEQUENCE_LEN)

strategy = items, n
if not isinstance(strategy, tuple):
    strategy = (strategy,)

import heapq
def expensive_items(items,n):
  expensive_items = heapq.nlargest(n, items, key=lambda s: s['price'])
  return expensive_items

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, expensive_items, *args)
