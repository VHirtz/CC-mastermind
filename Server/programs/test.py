from . import program
from . import api

class test(program.program):
    def run():
        while True:
            yield api.Print("This is a test")