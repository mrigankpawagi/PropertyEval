import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
my_list = lists(elements=just(1), min_size=1, max_size=MAX_SEQUENCE_LEN)
element = integers(min_value=MIN_INT, max_value=MAX_INT)

strategy = my_list, element
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def check_element(list,element):
  check_element=all(v== element for v in list)
  return check_element

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, check_element, *args)
