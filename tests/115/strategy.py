from limits.limits import *
from hypothesis.strategies import lists, integers, composite

@composite
def create_grid(draw):
    n = draw(integers(min_value=1, max_value=100))
    grid = draw(lists(lists(integers(min_value=0, max_value=1), min_size=n, max_size=n), min_size=n, max_size=n))
    return grid

grid = create_grid()
capacity = integers(min_value=1, max_value=10)

strategy = grid, capacity
