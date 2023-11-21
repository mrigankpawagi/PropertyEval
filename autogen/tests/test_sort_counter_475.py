import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
dict1 = dictionaries(keys=text(alphabet=string.ascii_letters), values=integers())

strategy = dict1
if not isinstance(strategy, tuple):
    strategy = (strategy,)

from collections import Counter
def sort_counter(dict1):
 x = Counter(dict1)
 sort_counter=x.most_common()
 return sort_counter

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, sort_counter, *args)
