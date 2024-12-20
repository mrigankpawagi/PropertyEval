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
                
tuplex = tuples(elements(one_of(integers(), text())), max_size=MAX_SEQUENCE_LEN)
tuple1 = one_of(integers(), text())

strategy = tuplex, tuple1
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def check_tuplex(tuplex,tuple1): 
  if tuple1 in tuplex:
    return True
  else:
     return False

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, check_tuplex, *args)
