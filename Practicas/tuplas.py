# -*- coding: utf-8 -*-

def caracterRepetido(char_sequence):
    mira_palabras = {}

    for idx, letter in enumerate(char_sequence):
        if letter not in mira_palabras:
            mira_palabras[letter] = (idx, 1)
        else:
            mira_palabras[letter] = (mira_palabras[letter][0], mira_palabras[letter][1]+1)

    final_letters = []
    for key, value in mira_palabras.items():
        if value[1] == 1:
            final_letters.append( (key, value[0]) )
    
    not_repeted_leters = sorted(final_letters, key=lambda value: value[1])

    if not_repeted_leters:
        return not_repeted_leters[0][0]
    else:
        return '_'

        

if __name__ == "__main__":
    char_sequence = str(input('Escribe una secuencia de caracteres: '))

    result = caracterRepetido(char_sequence)

    if result == '_':
        print('Todos los carcteres se repitenr')
    else:
        print('El primer caracter que no se repite es el siguiente: {}'.format(result))
