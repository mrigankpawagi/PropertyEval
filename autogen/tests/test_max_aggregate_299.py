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
                
@composite
def student_data(draw):
    n = draw(integers(min_value=1, max_value=MAX_SEQUENCE_LEN))
    data = [
        (draw(text(alphabet=characters(min_codepoint=65, max_codepoint=122, whitelist_categories=('Lu', 'Ll', 'Nd')))),
         draw(integers(min_value=0, max_value=100)))
        for _ in range(n)
    ]
    return data

stdata = student_data()
strategy = stdata
if not isinstance(strategy, tuple):
    strategy = (strategy,)

from collections import defaultdict
def max_aggregate(stdata):
    temp = defaultdict(int)
    for name, marks in stdata:
        temp[name] += marks
    return max(temp.items(), key=lambda x: x[1])

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, max_aggregate, *args)
