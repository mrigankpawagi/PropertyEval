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
                
import hypothesis.strategies as st

list_of_dicts = st.lists(st.dictionaries(st.text(), st.none()))
strategy = list_of_dicts
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def empty_dit(list1):
 empty_dit=all(not d for d in list1)
 return empty_dit

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, empty_dit, *args)
