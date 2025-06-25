# check the type of a coroutine
import asyncio
# define
async def custom_coro():
    # await
    await asyncio.sleep(1)

# create
coro = custom_coro()
#
print(type(coro))