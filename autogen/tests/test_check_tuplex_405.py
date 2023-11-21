import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
tuplex = tuples(integers(), integers(max_value=10), text(alphabet='abcdefghijklmnopqrstuvwxyz', min_size=1, max_size=1))
tuple1 = text(alphabet='abcdefghijklmnopqrstuvwxyz', min_size=1, max_size=1)

strategy = tuplex, tuple1
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def check_tuplex(tuplex,tuple1): 
  if tuple1 in tuplex:
    return True
  else:
     return False

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, check_tuplex, *args)
