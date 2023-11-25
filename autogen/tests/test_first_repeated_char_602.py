import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
str1 = text(alphabet="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", min_size=2, max_size=MAX_SEQUENCE_LEN)
strategy = str1
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def first_repeated_char(str1):
  for index,c in enumerate(str1):
    if str1[:index+1].count(c) > 1:
      return c

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, first_repeated_char, *args)
