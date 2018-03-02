# -*- coding: utf-8 -*_

def palindromo2(word):
    reversed_word = word[::-1]

    if reversed_word == word:
        return True
    
    return False




def palindromo(word):
    reversed_letters = []

    for letter in word:
        reversed_letters.insert(0, letter)

    reversed_word = ''.join(reversed_letters)

    if reversed_word == word:
        return True
    
    return False


if __name__ == '__main__':
    word = str(input('Escribe una palabra: '))

    result = palindromo2(word)

    if result is True:
        print('{} Si es un Palindromo'.format(word))
    else:
        print('{} No es un Palindromo'.format(word))