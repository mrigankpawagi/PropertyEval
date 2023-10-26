import sys; sys.path.append("../.."); from groundtruth_fuzzer.limits import MAX_INT, MIN_INT, MAX_FLOAT, MIN_FLOAT, MAX_SEQUENCE_LEN
from hypothesis.strategies import composite, lists, integers, permutations

@composite
def create_grid(draw, n_st=integers(min_value=2, max_value=MAX_SEQUENCE_LEN)):
    n = draw(n_st)
    grid = draw(lists(lists(integers(), min_size=n, max_size=n), min_size=n, max_size=n))
    
    perm = draw(permutations(range(1, n**2 + 1)))
    # fill grid with perm
    for i in range(n):
        for j in range(n):
            grid[i][j] = perm[i*n + j]
    
    return grid

grid = create_grid()
k = integers(min_value=1, max_value=MAX_INT)

strategy = grid, k
