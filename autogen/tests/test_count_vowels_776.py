import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
test_str = text(alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', min_size=1, max_size=MAX_SEQUENCE_LEN)

strategy = test_str
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def count_vowels(test_str):
  res = 0
  vow_list = ['a', 'e', 'i', 'o', 'u']
  for idx in range(1, len(test_str) - 1):
    if test_str[idx] not in vow_list and (test_str[idx - 1] in vow_list or test_str[idx + 1] in vow_list):
      res += 1
  if test_str[0] not in vow_list and test_str[1] in vow_list:
    res += 1
  if test_str[-1] not in vow_list and test_str[-2] in vow_list:
    res += 1
  return (res) 

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, count_vowels, *args)
