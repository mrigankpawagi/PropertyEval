from hypothesis.strategies import text, builds

def space_out(s: str):
    return " ".join(s)

test = builds(space_out, text(alphabet="abcde", max_size=5))

strategy = test
