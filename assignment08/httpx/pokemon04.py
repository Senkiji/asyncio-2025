import asyncio
import httpx

names = ["pikachu", "bulbasaur", "charmander", "squirtle", "eevee", "snorlax", "gengar", "mewtwo", "psyduck","jigglypuff"]

async def fetch_url(url):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json()
        return data
    
async def main():   
    tasks = [fetch_url(f"https://pokeapi.co/api/v2/pokemon/{name}") for name in names]
    results = await asyncio.gather(*tasks)

    for data in results:
        print(f"{data['name'].title()} -> ID: {data['id']}, Type(s): {[t['type']['name'] for t in data['types']]}")


asyncio.run(main())