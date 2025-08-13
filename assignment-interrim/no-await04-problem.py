import asyncio
import random
import time

async def save_to_db(sensor_id, value):
    await asyncio.sleep(1) # Simulate a database save operation
    if value > 80:
        raise ValueError(f"Value {value} for sensor {sensor_id} is too high!")
    print(f"{time.ctime()} Saved {sensor_id} = {value}")

async def handle_sensor(sensor_id):
    value = random.randint(50, 100)  # Simulate sensor reading
    print(f"{time.ctime()} Sensor {sensor_id} got value: {value}")
    asyncio.create_task(save_to_db(sensor_id, value))

async def main():
    for i in range(5):
        await handle_sensor(i)
    await asyncio.sleep(0.5)  # Allow time for all tasks to complete

asyncio.run(main())