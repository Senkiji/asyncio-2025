import asyncio
import httpx

names = ["pikachu", "bulbasaur", "charmander", "squirtle", "eevee", "snorlax", "gengar", "mewtwo", "psyduck","jigglypuff"]

async def fetch_url(url):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json()
        return data
    
def get_exp(data): #functionดึงค่า base_experience
    return data.get('base_experience')
    
async def main():   
    tasks = [fetch_url(f"https://pokeapi.co/api/v2/pokemon/{name}") for name in names]
    results = await asyncio.gather(*tasks)

    data_sorted = sorted(results, key=get_exp, reverse=True)

    for data in data_sorted:
        print(f"{data['name'].title()} -> ID: {data['id']}, Base Experience: {data['base_experience']}")


asyncio.run(main())