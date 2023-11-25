import heapq as hq
def heap_sort(iterable):
  """
  Write a function to sort the given list.
  """
  h = []
  for value in iterable:
    hq.heappush(h, value)
  return [hq.heappop(h) for i in range(len(h))]

def test_heap_sort():
  assert heap_sort([]) == []
  assert heap_sort([