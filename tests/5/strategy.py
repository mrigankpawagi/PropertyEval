from hypothesis.strategies import integers, lists

numbers = lists(integers())
delimiter = integers()

strategy = numbers, delimiter
