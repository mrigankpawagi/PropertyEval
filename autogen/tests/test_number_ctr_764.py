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
                
str = text(alphabet="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", min_size=0, max_size=MAX_SEQUENCE_LEN)
strategy = str
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def number_ctr(str):
      number_ctr= 0
      for i in range(len(str)):
          if str[i] >= '0' and str[i] <= '9': number_ctr += 1     
      return  number_ctr

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, number_ctr, *args)
