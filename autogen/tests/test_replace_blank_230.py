import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
str1 = text(min_size=1)
char = text(min_size=1)

strategy = str1, char
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def replace_blank(str1,char):
 str2 = str1.replace(' ', char)
 return str2

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, replace_blank, *args)
