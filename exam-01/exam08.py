# Hint:
# โค้ดนี้จะทำงานได้ แต่เกิด ResourceWarning: Unclosed client session
# ให้นักศึกษาแก้ไขโดยใช้ async with aiohttp.ClientSession()
# Result:
# 1256

import aiohttp
import asyncio

async def fetch(session, url):
    async with session.get(url) as resp:
        text = await resp.text()
        return text

async def main():
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, "https://example.com")
        print(len(html))

asyncio.run(main())
