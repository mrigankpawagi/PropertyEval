import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
tuplex = tuples(integers(), integers(), integers(), integers(), integers(), integers()).map(lambda t: t[:6])
m = integers(min_value=0, max_value=5)
n = integers(min_value=0, max_value=5)

strategy = tuplex, m, n
if not isinstance(strategy, tuple):
    strategy = (strategy,)

from copy import deepcopy
def colon_tuplex(tuplex,m,n):
  tuplex_colon = deepcopy(tuplex)
  tuplex_colon[m].append(n)
  return tuplex_colon

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, colon_tuplex, *args)
