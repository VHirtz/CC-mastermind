from . import program
from . import api

class dance(program.program):
    def run(self):
        while True:
            yield api.turtle.forward()
            yield "print('hello world')"
