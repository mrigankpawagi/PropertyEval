import heapq as hq
def heap_sort(iterable):
  """
  Write a function to sort the given list.
  >>> heap_sort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])==[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
  """
  h = []
  for value in iterable:
    hq.heappush(h, value)
  return [hq.heappop(h) for i in range(len(h))]

def merge_sort(iterable):
  """
  Write a function to sort the given list.
  >>>