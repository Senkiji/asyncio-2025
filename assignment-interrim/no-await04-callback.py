import asyncio
import time
import random

async def save_to_db(sensor_id, value):
    await asyncio.sleep(1)  # Simulate a database save operation
    if value > 80:
        raise ValueError(f"{sensor_id} value is too high!")
    print(f"{time.ctime()}{sensor_id} Saved value {value}")

def task_done_callback(task):
    try:
        result = task.result() 
        print(f"{time.ctime()} Task completed with result: {result}")
    except Exception as e:
        print(f"{time.ctime()} Task failed with exception: {e}")

async def handle_sensor(sensor_id):
    value = random.randint(50, 100)  # Simulate sensor reading
    print(f"{time.ctime()} Sensor {sensor_id} got value: {value}")
    
    task = asyncio.create_task(save_to_db(sensor_id, value))
    task.add_done_callback(task_done_callback)  # Add callback to handle completion

async def main():
    for i in range(5):
        await handle_sensor(i)
    await asyncio.sleep(1)  # Allow time for all tasks to complete

asyncio.run(main())