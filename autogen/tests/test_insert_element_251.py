import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
lst = lists(elements=text(), min_size=1, max_size=MAX_SEQUENCE_LEN)
element = text()

strategy = lst, element
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def insert_element(list,element):
 list = [v for elt in list for v in (element, elt)]
 return list

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, insert_element, *args)