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
                
tup1 = lists(elements=characters(max_codepoint=122, whitelist_categories=('Ll',)), min_size=1)
strategy = tup1.map(tuple)
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def tup_string(tup1):
  str =  ''.join(tup1)
  return str

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, tup_string, *args)
