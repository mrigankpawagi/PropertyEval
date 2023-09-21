from hypothesis.strategies import lists, integers

nums = lists(integers(min_value=-20, max_value=20), max_size=20)

strategy = nums
