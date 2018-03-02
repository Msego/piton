

import turtle


def main():
    window = turtle.Screen()
    tu = turtle.Turtle()

    make_square(tu)

    turtle.mainloop()


def make_square(tu):
    length = int(input('tamaño cuadrado'))
    
    for i in range(4):
        make_line_and_turn(dave, length)


def make_line_and_turn(tu, lenght):
    tu.forward(lenght)
    tu.left(90)


if __name__ == '__main__':
    main()