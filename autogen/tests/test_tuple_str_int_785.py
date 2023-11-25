import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
test_str = tuples(text(alphabet='123456789', min_size=1, max_size=1), text(alphabet='1234567890', min_size=1, max_size=1)).map(lambda t: f'({t[0]}, {t[1]})')
strategy = test_str
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def tuple_str_int(test_str):
  res = tuple(int(num) for num in test_str.replace('(', '').replace(')', '').replace('...', '').split(', '))
  return (res) 

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, tuple_str_int, *args)
