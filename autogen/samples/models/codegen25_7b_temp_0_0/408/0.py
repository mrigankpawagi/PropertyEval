import heapq
def k_smallest_pairs(nums1, nums2, k):
   queue = []
   def push(i, j):
  """
  Write a function to find k number of smallest pairs which consist of one element from the first array and one element from the second array.
  """
   heapq.heappush(queue, (nums1[i] + nums2[j], i, j))
   if len(queue) > k:
       heapq.heappop(queue)
   while queue:
       _, i, j = heapq.heappop(queue)
       if j