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
                
list_ = lists(integers(), max_size=MAX_SEQUENCE_LEN)
string = builds(lambda p, s: p + '{0}' + s, text(string.ascii_letters), text(string.ascii_letters))

strategy = list_, string
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def add_string(list_, string):
 add_string=[string.format(i) for i in  list_]
 return add_string

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, add_string, *args)
