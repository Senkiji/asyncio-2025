import asyncio,time

async def worker_long():
    print(f'{time.ctime()} [worker_long] Starting')
    try:
        await asyncio.sleep(5)  # Simulate a long-running task
        print(f'{time.ctime()} [worker_long] Done')
    except asyncio.CancelledError:
        print(f'{time.ctime()} [worker_long] Cancelled')

async def main():
    print(f'{time.ctime()} starting main loop...')
    asyncio.create_task(worker_long())
    await asyncio.sleep(1)  # Allow some time for the worker to run
    print(f'{time.ctime()} Main loop finished...')  

asyncio.run(main())