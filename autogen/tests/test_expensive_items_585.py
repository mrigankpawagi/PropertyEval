import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
@composite
def create(draw):
  n = draw(integers(min_value=1, max_value=MAX_SEQUENCE_LEN))
  item = builds(lambda name, price: {'name': name, 'price': price}, text(), floats(min_value=0.0, max_value=MAX_FLOAT))
  items = draw(lists(item, min_size=n, max_size=n))
  return items, n
items = shared(create(), key='eval').map(lambda x: x[0])
n = shared(create(), key='eval').map(lambda x: x[1])

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
