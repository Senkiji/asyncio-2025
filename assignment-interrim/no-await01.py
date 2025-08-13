import asyncio,time

async def worker_ok():
    print(f'{time.ctime()} [worker_ok] Starting')
    await asyncio.sleep(1)  # Simulate a short task
    print(f'{time.ctime()} [worker_ok] Done')

async def main():
    asyncio.create_task(worker_ok())
    await asyncio.sleep(2)  # Wait for the worker to finish

asyncio.run(main())