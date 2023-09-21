from hypothesis.strategies import lists, integers, composite, shared

@composite
def lst(draw):
    n = draw(integers(min_value=0, max_value=10))
    l1 = draw(lists(integers(min_value=-10, max_value=10), min_size=n, max_size=n))
    l2 = draw(lists(integers(min_value=-10, max_value=10), min_size=n, max_size=n))
    
    return l1, l2

ls = lst()
game = shared(ls, key='eval').map(lambda x: x[0])
guess = shared(ls, key='eval').map(lambda x: x[1])

strategy = game, guess
