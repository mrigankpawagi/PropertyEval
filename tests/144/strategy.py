from hypothesis.strategies import integers, builds

def frac(a, b):
    return f"{a}/{b}"

x = builds(frac, integers(min_value=1, max_value=20), integers(min_value=1, max_value=20))
n = builds(frac, integers(min_value=1, max_value=20), integers(min_value=1, max_value=20))

strategy = x, n
