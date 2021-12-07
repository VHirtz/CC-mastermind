import asyncio
import aiohttp
import requests
from aiohttp import web

import programs
import json
import pickle

class Computer:
    def __init__(self):
        self.initialized = False
        self.state = {}

    def saveState(self, pcid):
        file = open("./database/" + str(pcid), "wb")
        pickle.dump(self.state, file)
        file.close()
    
    def loadState(self, pcid):
        try:
            file = open("./database/" + str(pcid), "rb")
        except FileNotFoundError:
            return " "
        state = pickle.load(file)
        file.close
        self.state = state
        return None
    
    def run(self, msg):
        if not self.initialized:
            self.pcid = msg
            to_send = self.loadState(self.pcid)
            if to_send != None:
                return to_send
            self.object_instance = eval(
                "programs." + self.state["program"] + "." + self.state["program"])(self.state)
            self.program_instance = self.object_instance.run()
            self.initialized = True
        self.state["return"] = json.loads(msg)
        self.saveState(self.pcid)
        return next(self.program_instance)
