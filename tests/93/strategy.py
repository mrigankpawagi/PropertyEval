from hypothesis.strategies import text

message = text(alphabet="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ").filter(lambda s: s == " " or s.isalpha())

strategy = message
