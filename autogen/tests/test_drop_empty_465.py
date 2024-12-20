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
                
dict1 = dictionaries(keys=text(alphabet='abcde', max_size=5).map(lambda x: x if x != "" else None), values=one_of(text(alphabet='abcde'), none()))
strategy = dict1
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def drop_empty(dict1):
  dict1 = {key:value for (key, value) in dict1.items() if value is not None}
  return dict1

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, drop_empty, *args)
