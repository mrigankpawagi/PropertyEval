import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
import string

def dict_with_strings():
    return dictionaries(
        keys=text(
            alphabet=string.ascii_letters + string.digits,
            min_size=1,
            max_size=MAX_SEQUENCE_LEN,
        ),
        values=one_of(integers(), floats()),
        min_size=1,
        max_size=MAX_SEQUENCE_LEN,
    )

strategy = dict_with_strings()
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def return_sum(dict):
  sum = 0
  for i in dict.values():
    sum = sum + i
  return sum

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, return_sum, *args)
