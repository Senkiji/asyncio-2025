import time
import aiohttp
import asyncio

student_id = "6610301010"

async def fire_rocket(name: str, t0: float):
    url = f"http://172.16.2.117:8088/fire/{student_id}"
    start_time = time.perf_counter() - t0  # เวลาเริ่มสัมพัทธ์
    """
    TODO:
    - ส่ง GET request ไปยัง rocketapp ที่ path /fire/{student_id}
    - อ่านค่า time_to_target จาก response
    - return dict ที่มี:
        {
            "name": name,
            "start_time": start_time,
            "time_to_target": time_to_target,
            "end_time": end_time
        }
    """
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            data = await resp.json()
            time_to_target = data.get("time_to_target", 0)
    end_time = start_time + time_to_target
    return {
        "name": name,
        "start_time": start_time,
        "time_to_target": time_to_target,
        "end_time": end_time
    }
    pass

async def main():
    t0 = time.perf_counter()  # เวลาเริ่มของชุด rockets

    print("Rocket prepare to launch ...")  # แสดงตอนเริ่ม main

    # TODO: สร้าง task ยิง rocket 3 ลูกพร้อมกัน
    tasks = []
    for i in range(1, 4):
        tasks.append(asyncio.create_task(fire_rocket(f"Rocket-{i}", t0)))

    # TODO: รอให้ทุก task เสร็จและเก็บผลลัพธ์ตามลำดับ task
    results = []
    for t in tasks:
        results.append(await t)

    # TODO: แสดงผล start_time, time_to_target, end_time ของแต่ละ rocket ตามลำดับ task
    for r in results:
        pass  # แสดงผล rocket
        print(f"{r['name']}: start_time={r['start_time']:.2f}, time_to_target={r['time_to_target']:.2f}, end_time={r['end_time']:.2f}")

    # TODO: แสดงเวลารวมทั้งหมดตั้งแต่ยิงลูกแรกจนลูกสุดท้ายถึงจุดหมาย
    t_total = max(r['end_time'] for r in results)  # คำนวณ max end_time
    print(f"\nTotal time for all rockets: {t_total:.2f} sec")

asyncio.run(main())

