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
                
str1 = lists(text(max_size=10))
sub_str = text(max_size=10)

strategy = str1, sub_str
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def find_substring(str1, sub_str):
   if any(sub_str in s for s in str1):
       return True
   return False

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, find_substring, *args)
