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
                
a = integers(min_value=MIN_INT, max_value=MAX_INT)
b = integers(min_value=MIN_INT, max_value=MAX_INT)
c = integers(min_value=MIN_INT, max_value=MAX_INT)

strategy = a, b, c
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def min_of_three(a,b,c): 
      if (a <= b) and (a <= c): 
        smallest = a 
      elif (b <= a) and (b <= c): 
        smallest = b 
      else: 
        smallest = c 
      return smallest 

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, min_of_three, *args)
