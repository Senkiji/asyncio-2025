# Create 2 Tasks with High-Level API
import asyncio

async def download_image(name,delay):
    print(f"{name} กำลังโหลด . . .")
    await asyncio.sleep(delay)
    print(f"{name} โหลดเสร็จแล้วโว้ย!!!")

async def main():
    #
    task1 = asyncio.create_task(download_image("image1",2))
    task2 = asyncio.create_task(download_image("image1",2))

    #
    await task1
    await task2

asyncio.run(main())