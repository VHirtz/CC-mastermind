import asyncio
import aiohttp
import requests
from aiohttp import web

import programs
import database
import json

class Computer:
    def __init__(self):
        self.initialized = False
        self.state = {}

    def saveState(self, pcid):
        db = database.getDb()
        json_dump = json.dumps(self.state)
        binary = ' '.join(format(ord(letter), 'b') for letter in json_dump)
        db.put(str.encode(pcid), str.encode(binary))
    
    def loadState(self, pcid):
        db = database.getDb()
        binary = db.get(str.encode(pcid))
        if binary == None:
            print("No state for computer %s" % pcid)
            return ""
        else :
            json_dump = ''.join(chr(int(x, 2)) for x in binary.split())
            self.state = json.loads(json_dump)
        return None
    
    def run(self, msg):
        if not self.initialized:
            self.pcid = msg
            to_send = self.loadState(self.pcid)
            if to_send != None:
                return to_send
            self.program_instance = eval("programs." + self.state["program"] + "." + self.state["program"])(self.state)
            self.initialized = True
        self.state["return"] = msg # To be parsed
        self.saveState(self.pcid)
        return next(self.program_instance.run())
