import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
@composite
def generate_string(draw):
    n = draw(integers(min_value=1, max_value=MAX_SEQUENCE_LEN))
    s = draw(text(alphabet='0123456789', min_size=n, max_size=n))
    return s

s = generate_string()

strategy = s
if not isinstance(strategy, tuple):
    strategy = (strategy,)

from collections import defaultdict
def count_Substrings(s):
    n = len(s)
    count,sum = 0,0
    mp = defaultdict(lambda : 0)
    mp[0] += 1
    for i in range(n):
        sum += ord(s[i]) - ord('0')
        count += mp[sum - (i + 1)]
        mp[sum - (i + 1)] += 1
    return count

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, count_Substrings, *args)
