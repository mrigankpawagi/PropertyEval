import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
from typing import Dict, Tuple

@composite
def create_data(draw):
    n = draw(integers(min_value=1, max_value=10))
    students = {}
    for _ in range(n):
        name = draw(text(alphabet=characters(min_codepoint=97, max_codepoint=122), min_size=1, max_size=10))
        height = draw(floats(min_value=4.0, max_value=7.0, allow_nan=False, allow_infinity=False))
        weight = draw(integers(min_value=40, max_value=100))
        students[name] = (height, weight)
    return students

students = create_data()
h = floats(min_value=4.0, max_value=7.0, allow_nan=False, allow_infinity=False)
w = integers(min_value=40, max_value=100)

strategy = students, h, w
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def filter_data(students,h,w):
    result = {k: s for k, s in students.items() if s[0] >=h and s[1] >=w}
    return result    

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, filter_data, *args)
