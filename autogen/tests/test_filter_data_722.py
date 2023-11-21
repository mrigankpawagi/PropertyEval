import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
students = dictionaries(
    keys=text(alphabet=characters(min_codepoint=32, max_codepoint=126)),
    values=tuples(floats(min_value=0, max_value=10), integers(min_value=0, max_value=100)),
    min_size=1,
    max_size=10
)
h = floats(min_value=0, max_value=10)
w = floats(min_value=0, max_value=100)

strategy = students, h, w
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def filter_data(students,h,w):
    result = {k: s for k, s in students.items() if s[0] >=h and s[1] >=w}
    return result    

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, filter_data, *args)
