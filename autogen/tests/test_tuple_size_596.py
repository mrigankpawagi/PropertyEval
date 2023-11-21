import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
tuple_list = tuples(
    elements=one_of(integers(), text()),
    min_size=1,
    max_size=MAX_SEQUENCE_LEN
)

strategy = tuples_list
if not isinstance(strategy, tuple):
    strategy = (strategy,)

import sys 
def tuple_size(tuple_list):
  return (sys.getsizeof(tuple_list)) 

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, tuple_size, *args)
