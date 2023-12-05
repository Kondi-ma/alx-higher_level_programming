#!/usr/bin/python3
def multiple_returns(sentence):
    length_sn = len(sentence)
    1_char = sentence[0] if length_sn > 0 else "None"
    t = length_sn, 1_char
    return(t)

