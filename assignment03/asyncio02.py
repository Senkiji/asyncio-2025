# example of running a coroutine
import asyncio
# 
async def custom_coro():
    #
    await asyncio.sleep(1)

#main
async def main():
    #
    await custom_coro()

asyncio.run(main())

