from .. import api

class Program:
    def __init__(self, reference):
        self.last_return = reference
    
    def run():
        # For testing purposes
        while True:
            yield Api.print("Hello world!")
