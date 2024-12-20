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
                
str1 = text(min_size=1, max_size=MAX_SEQUENCE_LEN)
ch = text(min_size=1, max_size=1)
newch = text(min_size=1, max_size=1)

strategy = str1, ch, newch
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def replace_char(str1,ch,newch):
 str2 = str1.replace(ch, newch)
 return str2

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, replace_char, *args)
