from aiohttp import web

import socketio

path = 'dist'
sio = socketio.AsyncServer(async_mode='aiohttp')
app = web.Application()
sio.attach(app)

async def index(request):
    with open(f'./{path}/index.html') as f:
        return web.Response(text=f.read(), content_type='text/html')

app.router.add_get('/', index)
app.router.add_static('/', f'./{path}')

if __name__ == '__main__':
    web.run_app(app)
