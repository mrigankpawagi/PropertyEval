import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given, settings
from timeout import run_with_timeout
from typing import *

@composite
def create(draw):
  tuplex = draw(lists(integers() | text() | floats() | booleans() | lists(integers() | text() | floats() | booleans(), max_size=MAX_SEQUENCE_LEN), max_size=MAX_SEQUENCE_LEN).filter(lambda x: sum([isinstance(i, list) for i in x]) > 0).map(tuple))
  m = draw(sampled_from([i for i in range(len(tuplex)) if isinstance(tuplex[i], list)]))
  n = integers() | text() | floats() | booleans()
  return tuplex, m, n

tuplex = shared(create(), key='eval').map(lambda x: x[0])
m = shared(create(), key='eval').map(lambda x: x[1])
n = shared(create(), key='eval').map(lambda x: x[2])

strategy = tuplex, m, n
if not isinstance(strategy, tuple):
    strategy = (strategy,)

from copy import deepcopy
def colon_tuplex(tuplex,m,n):
  tuplex_colon = deepcopy(tuplex)
  tuplex_colon[m].append(n)
  return tuplex_colon

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, colon_tuplex, *args)
