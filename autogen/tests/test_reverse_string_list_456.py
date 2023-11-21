import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
stringlist = lists(text())

strategy = stringlist
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def reverse_string_list(stringlist):
    result = [x[::-1] for x in stringlist]
    return result

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, reverse_string_list, *args)
