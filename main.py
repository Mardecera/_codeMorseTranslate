import _dictionary as dictionary
from _logic import *

def main():
    try:
        while True:
            show_menu()
            option = int(input("> "))

            if option == 1  : code()
            elif option == 2: decode()
            elif option == 3: code_and_decode()
            elif option == 4: break

    except:
        print(msn_error_menu)

if __name__ == '__main__':
    main()