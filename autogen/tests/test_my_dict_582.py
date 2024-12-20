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
                
from hypothesis import strategies as st

dict1 = st.dictionaries(keys=st.text(), values=st.integers())
strategy = dict1,
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def my_dict(dict1):
  if bool(dict1):
     return False
  else:
     return True

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, my_dict, *args)
