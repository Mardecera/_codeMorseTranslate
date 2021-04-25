import _dictionary as dictionary
import _to_morse as uncode
from _messages import *
from _decorator import *

def main():
    try:
        while True:
            container('### SELECCIONA UNA OPCION ###', msn_menu)
            option = int(input("> "))

            if option == 1:
                text = str(input(msn_input_text))
                container('Output:', format_text(uncode.code_text(text)))

            elif option == 2:
                text = str(input(msn_input_text))
                container('Output:', format_text(uncode.decode_text(text)))
            
            elif option == 3:
                text_temp = ''
                text = str(input(msn_input_text))

                text_temp = uncode.code_text(text)
                container('Codificado:', format_text(text_temp))

                text_temp = uncode.decode_text(text_temp)
                container('Decodificado:', format_text(text_temp))

            elif option == 4: break

    except:
        print('\n')
        decorator_center(msn_error_menu)

if __name__ == '__main__':
    main()
