def min_k(test_list, K):
  """
  Write a function to find minimum k records from tuple list. https://www.geeksforgeeks.org/python-find-minimum-k-records-from-tuple-list/ - in this case a verbatim copy of test cases
  """
  # initialize heap
  heap = []
  # insert first K items into heap
  for i in range(K):
    heapq.heappush(heap, test_list[i])
  # loop through remaining items
  for i in range(K, len(test_list)):
    # if item is greater