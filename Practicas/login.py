# -*- coding:utf-8 -*-

def protected(func):

    def wrapper(password):
        if password == '1234':
            return func()
        else:
            print('tas equicocao sahval')

    return wrapper

@protected
def protected_func():
    print('Tu pass ta buena BRO!')



if __name__ == "__main__":
    password = str(input('Pon tu pass to fuelte: '))

    protected_func(password)