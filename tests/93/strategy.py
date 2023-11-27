from limits.limits import *
from hypothesis.strategies import text

message = text(alphabet="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ", max_size=MAX_SEQUENCE_LEN)

strategy = message
