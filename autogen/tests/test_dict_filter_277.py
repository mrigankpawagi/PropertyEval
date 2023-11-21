import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
from hypothesis import strategies as st

@st.composite
def dictionary_and_integer(draw):
    keys = st.text(min_size=1)
    values = st.integers()
    return draw(st.dictionaries(keys, values)), draw(st.integers(min_value=0))

strategy = dictionary_and_integer()
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def dict_filter(dict,n):
 result = {key:value for (key, value) in dict.items() if value >=n}
 return result

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, dict_filter, *args)
