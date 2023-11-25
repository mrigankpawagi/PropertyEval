import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
from collections.abc import Mapping
from hypothesis import strategies as st
import string

@st.composite
def dictionary_strategy(draw):
    depth = draw(st.integers(min_value=1, max_value=5))
    dictionary = {}
    for _ in range(depth):
        key = draw(st.text(alphabet=string.ascii_letters + string.digits, min_size=1, max_size=10))
        value = draw(st.recursive(st.floats(allow_nan=False, allow_infinity=False),
                                    lambda children: st.lists(children, min_size=1, max_size=5).map(tuple)))
        dictionary[key] = value

    return dictionary

strategy = dictionary_strategy()
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def dict_depth(d):
    if isinstance(d, dict):
        return 1 + (max(map(dict_depth, d.values())) if d else 0)
    return 0

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, dict_depth, *args)
