import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
listval = lists(elements=one_of(integers(), floats(), text()), unique=True, min_size=1)
strategy = listval
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def min_val(listval):
     min_val = min(i for i in listval if isinstance(i, int))
     return min_val

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, min_val, *args)
