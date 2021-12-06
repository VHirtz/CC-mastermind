import asyncio
import aiohttp
import requests
from aiohttp import web

async def ip_resolver(request):
  ip = requests.get('https://api.ipify.org').content.decode('utf8')
  return web.Response(text=ip)

async def websocket_handler(request):
  ws = web.WebSocketResponse(autoclose=False, max_msg_size=0)
  await ws.prepare(request)

  async for msg in ws:
    if msg.type == aiohttp.WSMsgType.TEXT:
      if msg.data == 'close':
        await ws.close()
      else:
        await ws.send_str(msg.data + '/answer')
    elif msg.type == aiohttp.WSMsgType.ERROR:
      print('Connection closed with exception %s' % ws.exception())

  print('Connection closed')

  return ws

def main():
  app = web.Application()
  app.add_routes([web.get('/', ip_resolver)])
  app.add_routes([web.get('/ws', websocket_handler)])

  web.run_app(app, port=80)

if __name__ == "__main__":
  main()
