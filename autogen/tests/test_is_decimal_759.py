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
                
num = decimals(allow_nan=False, allow_infinity=False, min_value=0, max_value=9999, places=2, as_string=True)

strategy = num
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def is_decimal(num):
    import re
    dnumre = re.compile(r"""^[0-9]+(\.[0-9]{1,2})?$""")
    result = dnumre.search(num)
    return bool(result)

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, is_decimal, *args)
