from . import api
from . import program

class turtle_test(program.program):
    def run(self):
        while True:
            yield api.turtle.forward()
            yield "os.sleep(3)"