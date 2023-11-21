import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
l1 = lists(text(min_size=1, alphabet=string.ascii_uppercase + string.digits), min_size=1)
l2 = lists(text(min_size=1), min_size=1)
l3 = lists(integers(min_value=0, max_value=100), min_size=1)

strategy = l1, l2, l3
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def convert_list_dictionary(l1, l2, l3):
     result = [{x: {y: z}} for (x, y, z) in zip(l1, l2, l3)]
     return result

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, convert_list_dictionary, *args)
