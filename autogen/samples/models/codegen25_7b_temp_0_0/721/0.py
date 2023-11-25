def maxAverageOfPath(cost):
  """
  Given a square matrix of size N*N given as a list of lists, where each cell is associated with a specific cost. A path is defined as a specific sequence of cells that starts from the top-left cell move only right or down and ends on bottom right cell. We want to find a path with the maximum average over all existing paths. Average is computed as total cost divided by the number of cells visited in the path.
  """
  n = len(cost)
  dp = [[0] * n for _ in range(n)]
  for i in range(n):
    for j in range(n):
      dp[i][j] = cost[i][j]
  for i in range(1, n):
    for j in range