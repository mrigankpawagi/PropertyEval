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
                
str1 = text(alphabet='abcdefghijklmnopqrstuvwxyz', min_size=1, max_size=MAX_SEQUENCE_LEN).flatmap(lambda s: fixed_dictionaries({"str1": just(s)}))
strategy = str1
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def first_repeated_char(str1):
  for index,c in enumerate(str1):
    if str1[:index+1].count(c) > 1:
      return c

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, first_repeated_char, *args)
