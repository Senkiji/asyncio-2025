# Create 1 Task with High-Level API
import asyncio

async def do_something():
    print("ทำงาน . . .")
    await asyncio.sleep(2)
    print("ทำงานเสร็จแล้ว!!!")

async def main():
    task = asyncio.create_task(do_something())
    await task

asyncio.run(main())