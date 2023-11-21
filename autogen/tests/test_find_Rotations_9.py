import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
string = text(alphabet=characters(min_codepoint=0, max_codepoint=255), min_size=1)

strategy = string
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
def test_fuzz(args):
    run_with_timeout(0.3, find_Rotations, *args)
