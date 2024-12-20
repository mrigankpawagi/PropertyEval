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
                
import sys

@composite
def tuple_list(draw):
    n = draw(integers(min_value=0, max_value=MAX_SEQUENCE_LEN))
    items = []
    for _ in range(n):
        item = draw(one_of(integers(), floats(), booleans()))
        items.append(item)
    return tuple(items)

strategy = tuple_list().map(lambda t: (t,))
if not isinstance(strategy, tuple):
    strategy = (strategy,)

import sys 
def tuple_size(tuple_list):
  return (sys.getsizeof(tuple_list)) 

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, tuple_size, *args)
