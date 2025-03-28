import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given, settings
from timeout import run_with_timeout
from typing import *
                
number = floats(min_value=1e-5)
strategy = number
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def babylonian_squareroot(number):
    if(number == 0):
        return 0;
    g = number/2.0;
    g2 = g + 1;
    while(g != g2):
        n = number/ g;
        g2 = g;
        g = (g + n)/2;
    return g;

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, babylonian_squareroot, *args)
