from . import api

class program:
    def __init__(self, reference):
        self.state = reference
    
    def run(self):
        # For testing purposes
        while True:
            yield api.Print("Hello world!")
