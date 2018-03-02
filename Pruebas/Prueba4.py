# -*- coding: UTF-8 -*-

def foreing_exchange_calculator(ammount):
    euros_col_rate = 166.386

    return euros_col_rate * ammount

def run():
    print('CALCULADORA DE DIVISAS')
    print('Convierte Dineros')
    print('')

    ammount = float(input('Ingresa la cantidad de Euros'))

    foreing_exchange_calculator(ammount)

    result = foreing_exchange_calculator(ammount)

    print('${} euros son ${} estas petas'.format(ammount,result))
    print('')

if __name__ == '__main__':

    run()
