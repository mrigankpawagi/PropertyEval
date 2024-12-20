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
                
monthnum3 = integers(min_value=1, max_value=12).filter(lambda x: x != 2 and x != 12)
strategy = monthnum3
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def check_monthnumber_number(monthnum3):
  return monthnum3==4 or monthnum3==6 or monthnum3==9 or monthnum3==11

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, check_monthnumber_number, *args)
