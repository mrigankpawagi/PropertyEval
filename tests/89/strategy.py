from hypothesis.strategies import text

string = text().filter(lambda s: s == '' or s.islower())

strategy = string
