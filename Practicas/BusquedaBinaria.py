# -*- coding: utf-8 -*-

def busqueda_binaria(numeros, numeroBuscado, bajo, alto):

    if bajo > alto:
        return False

    mid = ( bajo + alto ) // 2

    if numeros[mid] == numeroBuscado:
        return True
    elif numeros[mid] > numeroBuscado:
        return busqueda_binaria(numeros, numeroBuscado ,bajo , mid - 1)
    else:
        return busqueda_binaria(numeros, numeroBuscado, mid + 1 , alto)
        




if __name__ == '__main__':
    
    numeros = [ 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 11 , 12 , 13 , 14 , 15 , 16 , 17 , 18 , 19 , 20 , 21 , 23 , 24 ]

    numeroBuscado = int(input('Ingresa un unumero: '))

    resultado = busqueda_binaria(numeros, numeroBuscado,  0 , (len(numeros)-1))

    if resultado is True:
        print('El numeor si esta en la lista')
    else:
        print('El numero no esta en la lista')