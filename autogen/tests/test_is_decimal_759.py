import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
num = text() | integers().map(str) | floats(allow_nan=False, allow_infinity=False).map(str)
strategy = num
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def is_decimal(num):
    import re
    dnumre = re.compile(r"""^[0-9]+(\.[0-9]{1,2})?$""")
    result = dnumre.search(num)
    return bool(result)

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, is_decimal, *args)
