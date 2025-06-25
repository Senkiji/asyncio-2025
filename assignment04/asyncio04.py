# example of starting many tasks and getting access to all tasks
import time
import asyncio

async def download_image(name,delay):
    print(f"{time.ctime} {name} กำลังโหลด . . .")
    await asyncio.sleep(delay)
    print(f"{time.ctime} {name} โหลดเสร็จแล้วโว้ย!!!")

async def main():
    #
    print(f'{time.ctime()} main coroutine started')
    # 
    started_tasks = [asyncio.create_task(download_image(i,i)) for i in range(3)]
    await asyncio.sleep(0.1)
    for task in started_tasks:
        await task

asyncio.run(main())

