import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
text = text(alphabet=characters(min_codepoint=32, max_codepoint=126), min_size=1, max_size=MAX_STRING_LEN)

strategy = text
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def check_integer(text):
 text = text.strip()
 if len(text) < 1:
    return None
 else:
     if all(text[i] in "0123456789" for i in range(len(text))):
          return True
     elif (text[0] in "+-") and \
         all(text[i] in "0123456789" for i in range(1,len(text))):
         return True
     else:
        return False

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, check_integer, *args)
