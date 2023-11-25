import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
list_ = lists(text(), min_size=0, max_size=MAX_SEQUENCE_LEN)
string = text()

strategy = list_, string
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def add_string(list_, string):
 add_string=[string.format(i) for i in  list_]
 return add_string

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, add_string, *args)
