from hypothesis.strategies import text

string = text()
substring = text().filter(lambda s: len(s) > 0)

strategy = string, substring
