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
                
students = dictionaries(
    keys=text(alphabet=string.ascii_letters, min_size=1, max_size=10),
    values=tuples(floats(min_value=0.0, exclude_min=True, allow_nan=False),
                  integers(min_value=0, max_value=100)),
    min_size=1,
    max_size=MAX_SEQUENCE_LEN
)
h = floats(min_value=0.0, exclude_min=True, allow_nan=False)
w = integers(min_value=0, max_value=100)

strategy = students, h, w
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def filter_data(students,h,w):
    result = {k: s for k, s in students.items() if s[0] >=h and s[1] >=w}
    return result    

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, filter_data, *args)
