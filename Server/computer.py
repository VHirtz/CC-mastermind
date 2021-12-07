import asyncio
import aiohttp
import requests
from aiohttp import web

import programs
import database

class Computer:
    def __init__(self):
        self.initialized = False
        self.state = {}

    def saveState(self, pcid):
        db = database.getDb()
        json_dump = json.dumps(self.state)
        binary = ' '.join(format(ord(letter), 'b') for letter in json_dump)
        db.put(str.encode(pcid), binary)
    
    async def loadState(self, pcid):
        db = database.getDb()
        binary = db.get(str.encode(self.computerId))
        if binary == None:
            print("No state for computer %s" % self.computerId)
            return ""
        else :
            json_dump = ''.join(chr(int(x, 2)) for x in binary.split())
            self.state = json.loads(json_dump)
        return None
    
    def run(self, msg):
        if not self.initialized:
            to_send = self.loadState(msg)
            if to_send != None:
                return to_send
        self.state["return"] = msg # To be parsed
        program_instance = eval("program." + self.state["program"])(self.state)
        while True:
            yield program_instance.run()
