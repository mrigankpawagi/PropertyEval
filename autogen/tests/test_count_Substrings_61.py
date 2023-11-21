import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
def count_Substrings(string: str) -> int:
    """
    Count the number of substrings with the sum of digits equal to their length.

    Args:
        string: The input string.

    Returns:
        The count of substrings.

    Examples:
        >>> count_Substrings('112112')
        6
        >>> count_Substrings('111')
        6
    """
    pass
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
