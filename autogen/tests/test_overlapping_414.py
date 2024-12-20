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
                
list1 = lists(integers(), max_size=MAX_SEQUENCE_LEN)
list2 = lists(integers(), max_size=MAX_SEQUENCE_LEN)

strategy = list1, list2
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def overlapping(list1,list2):  
    for i in range(len(list1)): 
        for j in range(len(list2)): 
            if(list1[i]==list2[j]): 
                return True
    return False

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, overlapping, *args)
