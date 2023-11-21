import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
import sys
from hypothesis import strategies as st

tuple_list = st.tuples(elements=st.one_of(st.integers(), st.text(), st.floats()), min_size=0, max_size=10)

strategy = tuple_list
if not isinstance(strategy, tuple):
    strategy = (strategy,)

import sys 
def tuple_size(tuple_list):
  return (sys.getsizeof(tuple_list)) 

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, tuple_size, *args)
