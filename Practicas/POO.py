# -*- coding: utf-8 -*-


class Lamp:
    _LAMPS = ['''
          .
     .    |    ,
      \   '   /
       ` ,-. '
    --- (   ) ---
         \ /
        _|=|_
       |_____|
    ''',
    '''
         ,-.
        (   )
         \ /
        _|=|_
       |_____|
    ''']

    def __init__(self, _is_turnet_on):
        self._is_turnet_on = False

    def turn_on(self):
        self._is_turnet_on = True
        self._display_image()

    def turn_of(self):
        self._is_turnet_on = False
        self._display_image()

    def _display_image(self):
        if self._is_turnet_on:
            print(self._LAMPS[0])
        else:
            print(self._LAMPS[1])


def run():
    lamp = Lamp(_is_turnet_on=False)

    while True:
        command = str(input('''
            ¿Qué deseas hacer?

            [p]render
            [a]pagar
            [s]alir
        '''))

        if command == 'p':
            lamp.turn_on()
        elif command =='a':
            lamp.turn_of()
        else:
            break

        
if __name__ == '__main__':
    run()