import _dictionary as dictionary
from _normalize import *
from _messages import *

def del_break_line(string):
    acc_str = ''
    for i in range(len(string)):
        if string[i] == '\n':
            acc_str += ' '
        else:
            acc_str += string[i]
    
    return acc_str

def code_text(text):
    text = normalize(text)
    morse = ''
    for letter in text:
        morse += dictionary.morse[letter] + ' '
    return morse

def decode_text(text):
    text = del_break_line(text)
    morse_list = text.split(' ')
    acc_symbol = ''

    for symbol in morse_list:
        for item in dictionary.morse:
            if symbol == dictionary.morse[item]:
                acc_symbol += item
                break
    return acc_symbol