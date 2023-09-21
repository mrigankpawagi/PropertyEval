from hypothesis.strategies import lists, integers

nums = lists(integers(), min_size=1, max_size=10)

strategy = nums
