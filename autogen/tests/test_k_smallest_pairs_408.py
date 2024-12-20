import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given, settings
from timeout import run_with_timeout
from typing import *
                
nums1 = lists(integers(), max_size=MAX_SEQUENCE_LEN)
nums2 = lists(integers(), max_size=MAX_SEQUENCE_LEN)
k = integers(min_value=0, max_value=MAX_SEQUENCE_LEN)

strategy = nums1, nums2, k
if not isinstance(strategy, tuple):
    strategy = (strategy,)

import heapq
def k_smallest_pairs(nums1, nums2, k):
   queue = []
   def push(i, j):
       if i < len(nums1) and j < len(nums2):
           heapq.heappush(queue, [nums1[i] + nums2[j], i, j])
   push(0, 0)
   pairs = []
   while queue and len(pairs) < k:
       _, i, j = heapq.heappop(queue)
       pairs.append([nums1[i], nums2[j]])
       push(i, j + 1)
       if j == 0:
           push(i + 1, 0)
   return pairs

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, k_smallest_pairs, *args)
