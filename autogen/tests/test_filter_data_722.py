import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
students = dictionaries(keys=text(), values=tuples(floats(min_value=0.0, allow_infinity=False, allow_nan=False), floats(min_value=0.0, allow_infinity=False, allow_nan=False)))
h = floats(min_value=0.0, allow_infinity=False, allow_nan=False)
w = floats(min_value=0.0, allow_infinity=False, allow_nan=False)

strategy = students, h, w
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def filter_data(students,h,w):
    result = {k: s for k, s in students.items() if s[0] >=h and s[1] >=w}
    return result    

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, filter_data, *args)
