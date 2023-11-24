import heapq
def k_smallest_pairs(nums1, nums2, k):
   queue = []
   def push(i, j):
  """
  Write a function to find k number of smallest pairs which consist of one element from the first array and one element from the second array.
  >>> k_smallest_pairs([1,3,7],[2,4,6],2)==[[1, 2], [1, 4]]
  """
   if i < len(nums1) and j < len(nums2):
      heapq.heappush(queue, (nums1[i] + nums2[j], i, j))
   if len(queue) > k:
      heapq.heappop(queue)
   return queue

