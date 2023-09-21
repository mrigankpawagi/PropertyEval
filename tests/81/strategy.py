from hypothesis.strategies import floats, lists

grades = lists(floats(min_value=0.0, max_value=4.0))

strategy = grades
