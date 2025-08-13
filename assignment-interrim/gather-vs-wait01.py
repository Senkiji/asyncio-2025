import asyncio

async def task_ok(n):
    await asyncio.sleep(n)
    return f'Ok after {n}s'

async def task_error(n):
    await asyncio.sleep(n)
    raise ValueError(f'Error after {n}s')

async def demo_gather():
    print("\n=== gather: return values ===")
    results = await asyncio.gather(task_ok(1), task_ok(2), task_ok(3))
    print("gather results:", results)

    print("\n=== gather: error stop all ===")
    try:
        await asyncio.gather(task_ok(1), task_error(2), task_ok(3))
    except ValueError as e:
        print("gather caught error:", e)

    print("\n=== gather: return_exceptions=True ===")
    results = await asyncio.gather(task_ok(1), task_error(2), task_ok(3), return_exceptions=True)
    print("gather results with exceptions:", results)

async def main():
    await demo_gather()

asyncio.run(main())