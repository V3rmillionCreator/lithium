import json
import time
import asyncio
import aiohttp

async def gc_smasher():

    async with aiohttp.ClientSession() as session:

        with open('settings.json') as config:
            settings = json.load(config)

        token = settings.get('token')

        group = int(input('Group ID: '))
        headers = {'authorization': token}
        
        while True:
            async with session.put(f'https://discordapp.com/api/v8/channels/{group}/recipients/1337', headers=headers) as gc_smasher_put_request:
                print(gc_smasher_put_request.status)
                match gc_smasher_put_request.status:

                    case 429:
                        await asyncio.sleep(1)

                    case 200:
                        await asyncio.sleep(.5)

                    case 401:
                        print('Invalid token')
                        break

asyncio.run(gc_smasher())