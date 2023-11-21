import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
dict1 = dictionaries(keys=integers(), values=integers())

strategy = dict1
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def my_dict(dict1):
  if bool(dict1):
     return False
  else:
     return True

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, my_dict, *args)
