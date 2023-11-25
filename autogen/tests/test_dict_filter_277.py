import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
dict_strategy = dictionaries(keys=text(), values=integers())
n_strategy = integers()

strategy = dict_strategy, n_strategy
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def dict_filter(dict,n):
 result = {key:value for (key, value) in dict.items() if value >=n}
 return result

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, dict_filter, *args)
