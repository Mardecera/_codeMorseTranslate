from prettytable import PrettyTable
from _messages import *

def show_menu():
    box_menu = PrettyTable()
    box_menu.field_names = ['SELECCIONA UNA OPCION']
    box_menu.align['SELECCIONA UNA OPCION'] = 'l'
    box_menu.add_row([msn_menu])
    print(box_menu)

def show_rpt(title, content):
    box_menu = PrettyTable()
    box_menu.field_names = [title]
    box_menu.align[title] = 'l'
    box_menu.add_row([content])
    print(box_menu)

def format_text(string):
    format_str = ''

    for i in range(len(string)):
        if i % 50 == 0 and i != 0:
            format_str += '\n'
        else:
            format_str += string[i]
    
    return format_str