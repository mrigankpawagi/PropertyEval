import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
listval = lists(one_of(text(), integers()), min_size=1)

strategy = listval
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def max_val(listval):
     max_val = max(i for i in listval if isinstance(i, int)) 
     return(max_val)

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, max_val, *args)
