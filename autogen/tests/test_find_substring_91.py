import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
str1 = lists(text(min_size=1), min_size=1)
sub_str = text(min_size=1)

strategy = str1, sub_str
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def find_substring(str1, sub_str):
   if any(sub_str in s for s in str1):
       return True
   return False

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, find_substring, *args)
