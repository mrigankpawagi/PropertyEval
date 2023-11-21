import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
n = integers()

strategy = n
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def last_Digit(n) :
    return (n % 10) 

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, last_Digit, *args)
