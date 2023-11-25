import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
items = lists(integers(min_value=1, max_value=100), unique=True)
n = integers(min_value=1, max_value=10)

strategy = items, n
if not isinstance(strategy, tuple):
    strategy = (strategy,)

import heapq
def expensive_items(items,n):
  expensive_items = heapq.nlargest(n, items, key=lambda s: s['price'])
  return expensive_items

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, expensive_items, *args)
