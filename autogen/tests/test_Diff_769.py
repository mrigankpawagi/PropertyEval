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
                
li1 = lists(integers(), max_size=MAX_SEQUENCE_LEN)
li2 = lists(integers(), max_size=MAX_SEQUENCE_LEN)

strategy = li1, li2
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def Diff(li1,li2):
    return list(set(li1)-set(li2)) + list(set(li2)-set(li1))
 

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, Diff, *args)
