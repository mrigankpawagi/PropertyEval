import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
from typing import List, Tuple

def get_coordinates(coord: Tuple[int, int]) -> List[List[int]]:
    x, y = coord
    adjacent = [(x-1, y-1), (x-1, y), (x-1, y+1), (x, y-1), (x, y+1), (x+1, y-1), (x+1, y), (x+1, y+1)]
    return [[c[0], c[1]] for c in adjacent]

coord = tuples(integers(), integers())
strategy = coord
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def adjac(ele, sub = []): 
  if not ele: 
     yield sub 
  else: 
     yield from [idx for j in range(ele[0] - 1, ele[0] + 2) 
                for idx in adjac(ele[1:], sub + [j])] 
def get_coordinates(test_tup):
  return list(adjac(test_tup))

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, adjac, *args)
