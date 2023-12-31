import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
s = text(alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ', min_size=1)
strategy = s
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def upper_ctr(str):
    upper_ctr = 0
    for i in range(len(str)):
          if str[i] >= 'A' and str[i] <= 'Z': upper_ctr += 1
          return upper_ctr

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, upper_ctr, *args)
