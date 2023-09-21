from hypothesis.strategies import lists, integers, composite, shared

@composite
def arr_k(draw):
    arr = draw(lists(integers(), min_size=1, max_size=100))
    k = draw(integers(min_value=1, max_value=len(arr)))
    return arr, k

arr = shared(arr_k(), key='eval').map(lambda x: x[0])
k = shared(arr_k(), key='eval').map(lambda x: x[1])

strategy = arr, k
