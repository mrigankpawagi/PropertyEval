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
                
s = text(alphabet='abcde', max_size=MAX_SEQUENCE_LEN).filter(lambda x: x == "" or x.islower())
strategy = s
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def find_Rotations(str): 
    tmp = str + str
    n = len(str) 
    for i in range(1,n + 1): 
        substring = tmp[i: i+n] 
        if (str == substring): 
            return i 
    return n 

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, find_Rotations, *args)
