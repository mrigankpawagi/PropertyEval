import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
import string

s = text(alphabet=string.ascii_letters + string.punctuation, max_size=MAX_SEQUENCE_LEN)
strategy = s
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def number_ctr(str):
      number_ctr= 0
      for i in range(len(str)):
          if str[i] >= '0' and str[i] <= '9': number_ctr += 1     
      return  number_ctr

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, number_ctr, *args)
