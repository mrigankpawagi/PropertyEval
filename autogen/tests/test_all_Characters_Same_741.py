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
                
s = text(alphabet='abcdefghijklmnopqrstuvwxyz', min_size=1, max_size=1)
strategy = s
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def all_Characters_Same(s) :
    n = len(s)
    for i in range(1,n) :
        if s[i] != s[0] :
            return False
    return True

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, all_Characters_Same, *args)
