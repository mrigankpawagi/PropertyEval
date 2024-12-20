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
                
import string

dict_ = dictionaries(keys=text(alphabet=string.ascii_lowercase, min_size=1, max_size=10), values=integers(), min_size=1, max_size=10)
n = integers()

strategy = dict_, n
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def dict_filter(dict,n):
 result = {key:value for (key, value) in dict.items() if value >=n}
 return result

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, dict_filter, *args)
