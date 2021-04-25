import math

def decorator_center(string):
    lines, width = len_and_lines(string)
    space = width
    width += 6
    padding = ' ' * 2

    content_top = ('=' * width) + '\n'
    content = ''
    for line in lines:
        space_left = ' ' * math.ceil((space - len(line)) / 2)
        space_rigth = ' ' * math.floor((space - len(line)) / 2)
        content += '∥' + padding + space_left + line + space_rigth + padding + '∥' + '\n'
    content_down = '=' * width

    return [content_top, content, content_down]

def decorator_default(string):
    lines, width = len_and_lines(string)
    space = width
    width += 6
    padding = ' ' * 2

    content_top = ('=' * width) + '\n'
    content = ''
    for line in lines:
        space_rigth = ' ' * (space - len(line))
        content += '∥' + padding + line + space_rigth + padding + '∥' + '\n'
    content_down = '=' * width

    return [content_top, content, content_down]

def len_and_lines(string):
    len_max = 0
    paragraph_lines = string.split('\n')

    for line in paragraph_lines:
        if len_max < len(line):
            len_max = len(line)
            
    return paragraph_lines, len_max

def format_text(string):
    format_str = ''

    for i in range(len(string)):
        if i % 50 == 0 and i != 0:
            format_str += '\n'
        else:
            format_str += string[i]
    
    return format_str

def container(title, message):
    title = decorator_default(title)
    message = decorator_default(message)

    output = title[0] + title[1] + message[0] + message[1] + message[2]
    print(output)