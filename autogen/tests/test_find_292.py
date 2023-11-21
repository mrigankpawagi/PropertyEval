import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
n = integers()
m = integers(min_value=1)

strategy = n, m
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def find(n,m):  
    q = n//m 
    return (q)

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, find, *args)
