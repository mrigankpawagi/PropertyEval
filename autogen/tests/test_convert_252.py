import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
numbers = floats(min_value=-MAX_FLOAT, max_value=MAX_FLOAT)

strategy = numbers
if not isinstance(strategy, tuple):
    strategy = (strategy,)

import cmath  
def convert(numbers):    
  num = cmath.polar(numbers)  
  return (num) 

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, convert, *args)
