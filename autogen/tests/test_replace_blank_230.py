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
                
str1 = text(alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', min_size=1, max_size=MAX_SEQUENCE_LEN).filter(lambda x: ' ' in x)
char = sampled_from(["@", "$", "-"])

strategy = str1, char
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def replace_blank(str1,char):
 str2 = str1.replace(' ', char)
 return str2

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, replace_blank, *args)
