import asyncio

async def task_ok(n):
    await asyncio.sleep(n)
    return f'Ok after {n}s'

async def task_error(n):
    await asyncio.sleep(n)
    raise ValueError(f'Error after {n}s')

async def demo_wait():
    print("\n=== wait: check status ===")
    tasks = {asyncio.create_task(task_ok(1)), asyncio.create_task(task_ok(2))}
    done, pending = await asyncio.wait(tasks)
    print("done tasks:", [t.result() for t in done])
    print("pending",pending)

    print("\n=== wait: handle errors manually ===")
    tasks = {asyncio.create_task(task_ok(1)), asyncio.create_task(task_error(2))}
    done, pending = await asyncio.wait(tasks)
    for t in done:
        if t.exception():
            print("Error in task:", t.exception())
        else:
            print("Task result:", t.result())

    print("\n=== wait: FIRST_COMPLETED ===")
    tasks = {asyncio.create_task(task_ok(1)), asyncio.create_task(task_error(3))}
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    print("First completed task result:", [t.result() for t in done])
    print("Still pending:", len(pending) , "tasks(s)")

async def main():
    await demo_wait()

asyncio.run(main())