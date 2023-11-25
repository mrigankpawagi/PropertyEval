import heapq as hq
def heap_queue_largest(nums,n):
  """
  Write a function to find the n largest integers from a given list of numbers, returned in descending order.
  """
  heap = []
  for i in range(n):
    hq.heappush(heap,nums[i])
  for i in range(n,len(nums)):
    if nums[i] > heap[0]:
      hq.heappop(heap)
      hq.