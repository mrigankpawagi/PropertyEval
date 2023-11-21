import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
num = text(alphabet='0123456789.', min_size=3, max_size=10)
strategy = num.filter(lambda x: x.count('.') == 1 and len(x.split('.')[1]) == 2)
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
