import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
lst = lists(lists(integers()))

strategy = lst
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def Extract(lst): 
    return [item[0] for item in lst] 

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, Extract, *args)
