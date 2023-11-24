def maxAverageOfPath(cost):
  """
  Given a square matrix of size N*N given as a list of lists, where each cell is associated with a specific cost. A path is defined as a specific sequence of cells that starts from the top-left cell move only right or down and ends on bottom right cell. We want to find a path with the maximum average over all existing paths. Average is computed as total cost divided by the number of cells visited in the path.
  >>> maxAverageOfPath([[1, 2, 3], [6, 5, 4], [7, 3, 9]]) == 5.2
  """
  def maxAverageOfPathHelper(cost, i, j, memo):
    if (i, j) in memo:
      return memo[(i, j)]
    if i == len(cost) - 1 and j == len(cost[0]) - 1:
      memo[(i, j)] = cost[i][j