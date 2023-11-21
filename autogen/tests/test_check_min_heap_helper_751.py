import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
from typing import List

@composite
def generate_min_heap(draw, size):
    heap = []
    for i in range(size):
        heap.append(draw(integers()))
        if i > 0 and heap[i] < heap[(i-1)//2]:
            temp = heap[i]
            j = i
            while j > 0 and temp < heap[(j-1)//2]:
                heap[j] = heap[(j-1)//2]
                j = (j-1)//2
            heap[j] = temp
    return heap

arr = generate_min_heap(size=MAX_HEAP_SIZE)

strategy = arr
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def check_min_heap_helper(arr, i):
    if 2 * i + 2 > len(arr):
        return True
    left_child = (arr[i] <= arr[2 * i + 1]) and check_min_heap_helper(arr, 2 * i + 1)
    right_child = (2 * i + 2 == len(arr)) or (arr[i] <= arr[2 * i + 2] 
                                      and check_min_heap_helper(arr, 2 * i + 2))
    return left_child and right_child

def check_min_heap(arr):
  return check_min_heap_helper(arr, 0)

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, check_min_heap_helper, *args)
