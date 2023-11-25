import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
str1 = text(max_size=MAX_SEQUENCE_LEN)
ch = characters(whitelist_categories=['Lu', 'Ll', 'Nd'], min_codepoint=32, max_codepoint=126)
newch = characters(min_codepoint=32, max_codepoint=126)

strategy = str1, ch, newch
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def replace_char(str1,ch,newch):
 str2 = str1.replace(ch, newch)
 return str2

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, replace_char, *args)
