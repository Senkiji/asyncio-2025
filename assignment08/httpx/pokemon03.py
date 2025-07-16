import asyncio
import httpx

# urls = ["https://pokeapi.co/api/v2/pokemon/pikachu"]

async def main():
    async with httpx.AsyncClient() as client:
        responses = await client.get('https://pokeapi.co/api/v2/pokemon/pikachu')
        data = responses.json()
        print(f"Name: {data['name']}")
        print(f"ID: {data['id']}")
        print(f"Height: {data['height']}")
        print(f"Weight: {data['weight']}")
        print(f"Types: {[t['type']['name'] for t in data['types']]}")

asyncio.run(main())