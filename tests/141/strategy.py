from hypothesis.strategies import text, builds, integers, booleans

def generate(s1: str, s2: str, b: bool, n1: int, n2: int):
    if b:
        s2 = ['txt', 'exe', 'dll'][n1]
    
    if n2 == 1:
        s1 = s1[:len(s1)//2] + '.' + s1[len(s1)//2:]
    elif n2 == 2:
        s1 = s1[:len(s1)//2] + '.' + s1[len(s1)//2:] + '.'
    
    return s1 + '.' + s2

file_name = builds(generate, 
                   text(alphabet=" !/abcdeABCDE012345"),
                     text(alphabet=" !/abcdeABCDE012345"),
                        booleans(),
                            integers(min_value=0, max_value=2),
                                integers(min_value=0, max_value=2))

strategy = file_name
