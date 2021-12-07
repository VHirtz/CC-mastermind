import asyncio
import aiohttp
import requests
from aiohttp import web

import computer

async def ip_resolver(request):
  ip = requests.get('https://api.ipify.org').content.decode('utf8')
  return web.Response(text=ip)

async def websocket_handler(request):
  ws = web.WebSocketResponse(autoclose=False, max_msg_size=0)
  await ws.prepare(request)

  first = True

  pc = computer.Computer()
  async for msg in ws:
    if msg.type == aiohttp.WSMsgType.TEXT:
      command = pc.run(msg.data)
      await ws.send_str(command)
    elif msg.type == aiohttp.WSMsgType.ERROR:
      print('Connection closed with exception %s' % ws.exception())

  print('Connection closed')

  return ws

async def pushId(request):
  headers = request.headers.copy()
  pc = computer.Computer()
  pc.state = {}
  pc.state["pcid"] = headers["pcid"]
  pc.state["program"] = headers["program"]
  pc.saveState(headers["pcid"])
  return web.Response()

def main():
  app = web.Application()
  app.add_routes([web.get('/', ip_resolver)])
  app.add_routes([web.get('/ws', websocket_handler)])
  app.add_routes([web.get('/pushId', pushId)])

  web.run_app(app, port=80)

if __name__ == "__main__":
  main()
