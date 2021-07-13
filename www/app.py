import logging
import asyncio

from aiohttp import web
logging.basicConfig(level=logging.INFO)


async def index(request):
    await asyncio.sleep(0.5)
    return web.Response(body=b'<h1>Index</h1>', content_type='text/html', charset='utf-8')


async def hello(request):
    await asyncio.sleep(0.5)
    text = '<h1>hello, %s!</h1>' % request.match_info['name']
    return web.Response(body=text.encode('utf-8'))

#
# def index(request):
#     return web.Response(body=b'<h1>Awesome</h1>', headers={'content-type': 'text/html'})
#
#
# async def hello(request):
#     return web.Response(body=b"Hello, world")


async def init():
    app = web.Application()
    app.router.add_get('/', index)

    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '127.0.0.1', 8000)
    await site.start()
    # srv = await loop.create_server(app.make_handler(), '127.0.0.1', 9000)

    # app_runner = web.AppRunner(app)
    # await app_runner.setup()
    # srv = await my_loop.create_server(app_runner.server, '127.0.0.1', 8000)

    # app = web.Application()
    # app.router.add_route('GET', '/', hello)
    # runner = web.AppRunner(app)
    # await runner.setup()
    # site = web.TCPSite(runner, '127.0.0.1', 9000)
    # await site.start()

    logging.info('server started at http://127.0.0.1:8000...')

    return site


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(init())
    loop.run_forever()











