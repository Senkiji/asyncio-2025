import asyncio,time

async def worker_error():
    print(f'{time.ctime()} [worker_error] Starting')
    await asyncio.sleep(1)
    raise ValueError("Boom!") # raise error

async def main():
    asyncio.create_task(worker_error())
    await asyncio.sleep(2)  # wait for the worker to finish

asyncio.run(main())