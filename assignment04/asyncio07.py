# get result
import asyncio

async def simple_task():
    await asyncio.sleep(1)
    return "โหลดเสร็จแล้ว"

async def main():
    task = asyncio.create_task(simple_task())
    await task
    print("ผลลัพธ์ของ Task:", task.result())

asyncio.run(main())