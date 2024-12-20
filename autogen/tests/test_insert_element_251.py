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
                
list_ = lists(sampled_from(['Red', 'Green', 'Black', 'python', 'java', 'happy', 'sad']), min_size=1, max_size=MAX_SEQUENCE_LEN)
element = text(alphabet='abcdefghijklmnopqrstuvwxyz', min_size=1, max_size=1)

strategy = list_, element
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def insert_element(list,element):
 list = [v for elt in list for v in (element, elt)]
 return list

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, insert_element, *args)
