import asyncio,time,random

async def get_temperature():
    await asyncio.sleep(random.uniform(0.5, 2.0))  # Simulate sensor reading delay
    return f"Temp: 30°C"

async def get_humidity():
    await asyncio.sleep(random.uniform(0.5, 2.0))  # Simulate sensor reading delay
    return f"Humidity: 60%"

async def get_weather_api():
    await asyncio.sleep(random.uniform(0.5, 2.0))  # Simulate API call delay
    return f"Weather API: Sunny"

async def main():
    start = time.time()
    current_time = time.ctime()
    temperature_task = asyncio.create_task(get_temperature())
    humidity_task = asyncio.create_task(get_humidity())
    weather_task = asyncio.create_task(get_weather_api())
    done,pending = await asyncio.wait([temperature_task, humidity_task, weather_task], return_when=asyncio.ALL_COMPLETED)
    for task in done:
        print(current_time,task.result())
    end = time.time()
    print(f"Took {end - start:.2f} seconds.")

asyncio.run(main())