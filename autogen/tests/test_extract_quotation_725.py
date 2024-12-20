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
                
text1 = text(alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ', max_size=MAX_SEQUENCE_LEN)
strategy = text1
if not isinstance(strategy, tuple):
    strategy = (strategy,)

import re
def extract_quotation(text1):
  return (re.findall(r'"(.*?)"', text1))

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, extract_quotation, *args)
