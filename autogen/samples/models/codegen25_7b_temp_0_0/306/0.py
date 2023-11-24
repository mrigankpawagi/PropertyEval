def max_sum_increasing_subseq(a, n, index, k):
  """
  Write a function to find the maximum sum of increasing subsequence from prefix until ith index and also including a given kth element which is after i, i.e., k > i .
  >>> max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 6) == 11
  """
  if index == n:
    return 0
  if k > index:
    return max_sum_increasing_subseq(a, n, index + 1, k)
  return max(max_sum_increasing_subseq(a, n, index + 1, k), a[index] + max_sum_increasing_sub