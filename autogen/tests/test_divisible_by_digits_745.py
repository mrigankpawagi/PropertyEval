import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
startnum = integers(min_value=1)
endnum = integers(min_value=1)

strategy = startnum, endnum
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def divisible_by_digits(startnum, endnum):
    return [n for n in range(startnum, endnum+1) \
                if not any(map(lambda x: int(x) == 0 or n%int(x) != 0, str(n)))]

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, divisible_by_digits, *args)
