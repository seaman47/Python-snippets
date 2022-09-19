# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 18:38:14 2022
@author: kbolo
"""

abs_morse = dict((('A', '.-'), ('B', '-...'), ('C', '-.-.'), ('D', '-..'), ('E', '.'), ('F', '..-.'), ('G', '--.'), ('H', '....'), ('I', '..'), ('J', '.---'), ('K', '-.-'), ('L', '.-..'), ('M', '--'), ('N', '-.'), ('O', '---'), ('P', '.--.'), ('Q', '--.-'), ('R', '.-.'), ('S', '...'), ('T', '-'), ('U', '..-'), ('V', '...-'), ('W', '.--'), ('X', '-..-'), ('Y', '-.--'), ('Z', '--..'), ('1', '.----'), ('2', '..---'), ('3', '...--'), ('4', '....-'), ('5', '.....'), ('6', '-....'), ('7', '--...'), ('8', '---..'), ('9', '----.'), ('0', '-----')))


def abc_morse(text):
    '''from ABC to Morse'''
    text = text.replace(' ', '/').upper()
    return ''.join(i+' ' if i == '/' else '* ' if i not in abs_morse else abs_morse[i]+' ' for i in text)


def morse_abc(text):
    '''from Morse to ABC'''
    morse_abc = {abs_morse[i]:i for i in abs_morse}
    text = text.split()
    return ''.join(' ' if i == '/' else '*' if i not in morse_abc else morse_abc[i] for i in text)

'TEST'
print(abc_morse('MY HOVERCRAF*T IS FULL OF EELS*'))
print(morse_abc('-- -.-- / .... --- ...- . .-. -.-. .-. .- ..-. * - / .. ... / ..-. ..- .-.. .-.. / --- ..-. / . . .-.. ... *'))