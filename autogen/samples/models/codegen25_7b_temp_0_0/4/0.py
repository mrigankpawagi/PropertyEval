import heapq as hq
def heap_queue_largest(nums,n):
  """
  Write a function to find the n largest integers from a given list of numbers, returned in descending order.
  >>> heap_queue_largest( [25, 35, 22, 85, 14, 65, 75, 22, 58],3)==[85, 75, 65]
  """
  hq.heapify(nums)
  largest = []
  for i in range(n):
    largest.append(hq.heappop(nums))
  return largest

def heap_queue_smallest(nums,n):
  """
  Write a function to find the n smallest integers from