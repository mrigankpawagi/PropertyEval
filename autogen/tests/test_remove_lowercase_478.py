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
                
str1 = text(alphabet='abcdefghijklmnopqrstuvwxyz', min_size=1, max_size=MAX_SEQUENCE_LEN).map(lambda x: x.upper())
strategy = str1
if not isinstance(strategy, tuple):
    strategy = (strategy,)

import re
def remove_lowercase(str1):
 return re.sub('[a-z]', '', str1)

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, remove_lowercase, *args)
