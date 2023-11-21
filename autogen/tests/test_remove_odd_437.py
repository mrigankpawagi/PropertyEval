import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
str1 = text(alphabet='abcdefghijklmnopqrstuvwxyz', min_size=1, max_size=MAX_SEQUENCE_LEN)

strategy = str1
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def remove_odd(str1):
 str2 = ''
 for i in range(1, len(str1) + 1):
    if(i % 2 == 0):
        str2 = str2 + str1[i - 1]
 return str2

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, remove_odd, *args)
