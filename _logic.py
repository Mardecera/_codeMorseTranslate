from _messages import *
from _to_morse import *
from _pretty import *

def code():
    text = str(input(msn_input_text))
    show_rpt('Output:', format_text(code_text(text)))

def decode():
    text = str(input(msn_input_text))
    show_rpt('Output:', format_text(decode_text(text)))

def code_and_decode():
    text = str(input(msn_input_text))

    txt_code, txt_decode = code_decode(text)
    show_rpt('Codificado: ', format_text(txt_code))
    show_rpt('Decodificado: ', format_text(txt_decode))