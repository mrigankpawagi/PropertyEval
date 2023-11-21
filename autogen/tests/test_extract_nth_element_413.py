import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
list1 = lists(tuples(tuples(text(alphabet=string.ascii_letters, min_size=1, max_size=20), integers(min_value=0, max_value=100), integers(min_value=0, max_value=100)))).filter(lambda x: len(x) > 0)
n = integers(min_value=0)

strategy = list1, n
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def extract_nth_element(list1, n):
    result = [x[n] for x in list1]
    return result

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, extract_nth_element, *args)
