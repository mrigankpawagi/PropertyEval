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
                
l = lists(elements=choice(["green", "orange", "black", "white", 1, 2, 3, 4]), max_size=MAX_SEQUENCE_LEN)
element = elements(choice(["green", "orange", "black", "white", 1, 2, 3, 4]))

strategy = l, element
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def check_element(list,element):
  check_element=all(v== element for v in list)
  return check_element

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, check_element, *args)
