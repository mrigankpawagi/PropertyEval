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
                
l = integers(min_value=1, max_value=MAX_INT)
strategy = l
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def surfacearea_cube(l):
  surfacearea= 6*l*l
  return surfacearea

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, surfacearea_cube, *args)
