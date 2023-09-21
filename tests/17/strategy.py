from hypothesis.strategies import text, sampled_from, lists

music_string = lists(sampled_from(["o", "o|", ".|"])).map(lambda s: " ".join(s))
                                            
strategy = music_string
