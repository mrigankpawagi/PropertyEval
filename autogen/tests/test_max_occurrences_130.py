import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
from collections import Counter

items = lists(integers(), min_size=1, max_size=MAX_SEQUENCE_LEN)
max_freq_item = items.flatmap(lambda lst: just(Counter(lst).most_common(1)[0][0]))

strategy = max_freq_item
if not isinstance(strategy, tuple):
    strategy = (strategy,)

from collections import defaultdict
def max_occurrences(nums):
    dict = defaultdict(int)
    for i in nums:
        dict[i] += 1
    result = max(dict.items(), key=lambda x: x[1]) 
    return result[0]

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, max_occurrences, *args)
