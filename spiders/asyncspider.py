#/usr/bin/env python
import asyncio
import aiohttp


NUMBERS = range(12)
URL = 'http://httpbin.org/get?a={}'

sema = asyncio.Semaphore(3)

async def fetch_async(a):
    try:
        async with aiohttp.ClientSession() as s:
            async with s.get(URL.format(a)) as resp:
                data = await resp.json()
        return data['args']['a']
    except Exception as e:
        print(e)
    

async def print_result(a):
    with (await sema):
        r = await fetch_async(a)
        print('fetch({}) = {}'.format(a,r))

loop = asyncio.get_event_loop()
f = asyncio.wait([print_result(num) for num in NUMBERS])
loop.run_until_complete(f)