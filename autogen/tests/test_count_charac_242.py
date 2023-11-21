import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
str1 = text(alphabet=characters(), min_size=1, max_size=MAX_STRING_LEN)

strategy = str1
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def count_charac(str1):
 total = 0
 for i in str1:
    total = total + 1
 return total

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, count_charac, *args)
