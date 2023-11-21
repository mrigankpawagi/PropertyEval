import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
from collections import defaultdict

@composite
def create_string(draw):
    size = draw(integers(min_value=1, max_value=100))
    string = draw(text(alphabet='123456789', min_size=size, max_size=size))
    return string

def count_Substrings(string: str) -> int:
    count = 0
    prefix_sum = defaultdict(int)
    prefix_sum[0] = 1
    current_sum = 0
    
    for digit in string:
        current_sum += int(digit)
        count += prefix_sum[current_sum - len(string)]
        prefix_sum[current_sum] += 1
    
    return count

string = create_string()

strategy = string
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
