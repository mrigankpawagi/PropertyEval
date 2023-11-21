import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
from hypothesis import strategies as st

def dict_filter(dictionary: Dict[str, int], n: int) -> Dict[str, int]:
    return {k: v for k, v in dictionary.items() if v >= n}

dictionary = st.dictionaries(st.text(min_size=1), st.integers())
n = st.integers()

strategy = dictionary, n
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def dict_filter(dict,n):
 result = {key:value for (key, value) in dict.items() if value >=n}
 return result

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, dict_filter, *args)
