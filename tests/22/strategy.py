from hypothesis.strategies import one_of, lists, integers, floats, sets, dictionaries, text, booleans, tuples, functions, binary, complex_numbers, none
# any other type?

hashable_types = (integers(), floats(), booleans(), text(), binary(), complex_numbers())
other_types = (none(), functions())

strategy = lists(one_of(*(hashable_types + other_types + (lists(one_of(*hashable_types)), sets(one_of(*(hashable_types + other_types))), dictionaries(one_of(*hashable_types), one_of(*(hashable_types + other_types))), tuples(one_of(*(hashable_types + other_types)))))))
