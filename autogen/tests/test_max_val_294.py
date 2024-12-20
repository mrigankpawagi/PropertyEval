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
                
listval = lists(elements=one_of(text(alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', max_size=10),
                                 integers(min_value=-1000, max_value=1000)),
                max_size=MAX_SEQUENCE_LEN)
strategy = listval
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def max_val(listval):
     max_val = max(i for i in listval if isinstance(i, int)) 
     return(max_val)

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, max_val, *args)
