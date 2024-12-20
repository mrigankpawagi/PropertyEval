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
                
text = text(alphabet='abcdefghij,.' ,max_size=MAX_SEQUENCE_LEN)
strategy = text
if not isinstance(strategy, tuple):
    strategy = (strategy,)

import re
def replace_specialchar(text):
 return (re.sub("[ ,.]", ":", text))


@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, replace_specialchar, *args)
