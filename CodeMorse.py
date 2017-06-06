#!/usr/bin/env python
# -*- coding: utf-8 -*-
morse = {'A' : ' . _ ', 	    'a' : ' . _ ',
         'B' : ' _ . . . ', 	'b' : ' _ . . . ',
         'C' : ' _ . _ . ', 	'c' : ' _ . _ . ',
         'D' : ' _ . . ', 	    'd' : ' _ . . ',
         'E' : ' . ', 	        'e' : ' . ',
         'F' : ' . . _ . ', 	'f' : ' . . _ . ',
         'G' : ' _ _ . ', 	    'g' : ' _ _ . ',
         'H' : ' . . . . ', 	'h' : ' . . . . ',
         'I' : ' . . ', 	    'i' : ' . . ',
         'J' : ' . _ _ _ ',     'j' : ' . _ _ _ ',
         'K' : ' _ . _ ', 	    'k' : ' _ . _ ',
         'L' : ' . _ . . ', 	'l' : ' . _ . . ',
         'M' : ' _ _ ', 	    'm' : ' _ _ ',
         'N' : ' _ . ', 	    'n' : ' _ . ',
         'Ñ' : ' _ _ . _ _ ',   'ñ' : ' _ _ . _ _ ',
         'O' : ' _ _ _ ',       'o' : ' _ _ _ ',
         'P' : ' . _ _ . ',     'p' : ' . _ _ . ',
         'Q' : ' _ _ . _ ',     'q' : ' _ _ . _ ',
         'R' : ' . _ . ', 	    'r' : ' . _ . ',
         'S' : ' . . . ', 	    's' : ' . . . ',
         'T' : ' _ ', 	        't' : ' _ ',
         'U' : ' . . _ ', 	    'u' : ' . . _ ',
         'V' : ' . . . _ ', 	'v' : ' . . . _ ',
         'W' : ' . _ _ ', 	    'w' : ' . _ _ ',
         'X' : ' _ . . _ ', 	'x' : ' _ . . _ ',
         'Y' : ' _ . _ _ ',     'y' : ' _ . _ _ ',
         'Z' : ' _ _ . . ',     'z' : ' _ _ . . ',
         '0' : ' _ _ _ _ _ ',     0 : ' _ _ _ _ _ ',
         '1' : ' . _ _ _ _ ',     1 : ' . _ _ _ _ ',
         '2' : ' . . _ _ _ ',     2 : ' . . _ _ _ ',
         '3' : ' . . . _ _ ',     3 : ' . . . _ _ _ ',
         '4' : ' . . . . _ ',	  4 : ' . . . . _ ',
         '5' : ' . . . . . ',     5 : ' . . . . . ',
         '6' : ' _ . . . . '  ,   6 : ' _ . . . . ',
         '7' : ' _ _ . . . ',     7 : ' _ _ . . . ',
         '8' : ' _ _ _ . . ',     8 : ' _ _ _ . . ',
         '9' : ' _ _ _ _ . ',     9 : ' _ _ _ _ . ',
         '.' : ' . _ . _ . _ ',
         ',' : ' _ . _ . _ _',
         '?' : ' . . _ _ . . ',
         '"' : ' . _ . . _ . ',
         '!' : ' _ _ . . _ _ ',
         ' ' : ' | '
         }

text = {'._' : 'A',
		'_...' : 'B',
		}

def decodeT(sentence):
	new = ""
	for i in range(len(sentence)):
		new += morse[sentence[i]];
	return new

def decodeM(sentence):
    new = ""
    word = ""
    for i in range(len(sentence)):
    	new += sentence[i]
    	if(new in text):
      		word += text[new]
      		new = ""
    return word

def main():
	sentence = ""
	print("1. De Texto a Morse.")
	print("2. De Morse a Texto.")

	option = int(input("Elija opcion: "))

	if(option == 1):
		sentence = str(input("Ingrese su texto: "))
		print("Morse :", decodeT(sentence))
	elif(option == 2):
		sentence = str(input("Ingrese su morse: "))
		print("Texto: ", decodeM(sentence))
	else:
		print("ERROR DE INGRESO.")

if __name__=='__main__':
	main()
