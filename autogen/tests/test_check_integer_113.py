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
                
text = text(alphabet='0123456789', min_size=1, max_size=MAX_SEQUENCE_LEN)
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
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, check_integer, *args)
