# file: rocketapp.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import asyncio
import random
import time

app = FastAPI(title="Asynchronous Rocket Launcher")

SERVER_NAME = "http://localhost:8000"


# Module
class Rocket(BaseModel):
    student_id: str
    launch_time: float

# เก็บ task ของจรวด (optional)
rockets = []

async def launch_rocket(student_id: str):
    """
    TODO:
    - จำลองเวลาจรวดด้วย random delay 1-2 วินาที
    - print log ว่า rocket launched และ reached destination
    """
    delay = random.uniform(1, 2)
    await asyncio.sleep(delay)
    print(f"Rocket launched by {student_id}")
    print(f"Rocket by {student_id} reached destination")
    return delay
    pass

@app.get("/fire/{student_id}")
async def fire_rocket(student_id: str):
    """
    TODO:
    - ตรวจสอบ student_id ต้องเป็น 10 หลัก
    - สร้าง background task ยิง rocket
    - รอ random delay 1-2 วินาที ก่อนส่ง response
    - return dict {"message": ..., "time_to_target": ...}
    """
    if len(student_id) != 10 or not student_id.isdigit():
        raise HTTPException(status_code=400, detail="Invalid student ID")
    start_time = time.time()
    task = asyncio.create_task(launch_rocket(student_id))
    rockets.append(task)
    time_to_target = await task
    end_time = time.time()
    return {"message": f"Rocket launched by {student_id}", "time_to_target": time_to_target}
    pass
