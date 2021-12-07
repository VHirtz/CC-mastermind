from . import program
from . import api

class turtle_dance(program.program):
    def run(self):
        yield api.turtle.forward()
        yield "print('hello world')"
