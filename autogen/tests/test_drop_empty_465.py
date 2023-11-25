import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
dict1 = dictionaries(keys=text(alphabet='abcdefghijklmnopqrstuvwxyz', max_size=10),
                        values=text(alphabet='abcdefghijklmnopqrstuvwxyz', max_size=MAX_SEQUENCE_LEN))
strategy = dict1
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def drop_empty(dict1):
  dict1 = {key:value for (key, value) in dict1.items() if value is not None}
  return dict1

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, drop_empty, *args)
