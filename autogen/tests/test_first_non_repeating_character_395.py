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
                
from collections import Counter

str1 = text(alphabet='abcdefghijklmnopqrstuvwxyz', max_size=MAX_SEQUENCE_LEN)

# Create a dictionary to keep track of character counts
def count_chars(s):
    return Counter(s)

# Retrieve the first non-repeating character
def get_first_non_repeating_char(s):
    char_order = []
    ctr = {}
    for c in s:
        if c in ctr:
            ctr[c] += 1
        else:
            ctr[c] = 1 
            char_order.append(c)
    for c in char_order:
        if ctr[c] == 1:
            return c
    return None

strategy = str1.map(lambda s: (s, count_chars(s))).filter(lambda x: get_first_non_repeating_char(x[0]) == x[1])
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def first_non_repeating_character(str1):
  char_order = []
  ctr = {}
  for c in str1:
    if c in ctr:
      ctr[c] += 1
    else:
      ctr[c] = 1 
      char_order.append(c)
  for c in char_order:
    if ctr[c] == 1:
      return c
  return None

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, first_non_repeating_character, *args)
