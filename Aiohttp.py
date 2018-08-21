from aiohttp import web


# async def index(request):
#     return web.Response(text='<h1>Index</h1>')

async def hello(request):
    text = '<h1>hello, %s!</h1>' % request.match_info.get('name', '访客')
    return web.Response(text=text)


app = web.Application()
app.add_routes([web.get('/', handler=hello),
                web.get('/{name}', hello)])

web.run_app(app=app, host='127.0.0.1', port=8001)
print('Server started at http://127.0.0.1:8000...')
