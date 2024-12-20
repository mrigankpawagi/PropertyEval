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
                
list1 = lists(tuples(text(max_size=10), integers(), integers()), max_size=MAX_SEQUENCE_LEN)
n = integers(min_value=0)

strategy = list1, n
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def extract_nth_element(list1, n):
    result = [x[n] for x in list1]
    return result

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, extract_nth_element, *args)
