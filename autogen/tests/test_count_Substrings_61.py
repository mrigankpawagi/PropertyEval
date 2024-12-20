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
                
s = text(alphabet='0123456789', min_size=1, max_size=MAX_SEQUENCE_LEN)
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
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, count_Substrings, *args)
