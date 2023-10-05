import asyncio
import aiohttp
import aiofiles
 
async def fetch(url):
    async with aiohttp.ClientSession() as session:
        response = await session.get(url) 
        html = await response.text()
        return html
 
async def write_to_file(file, text):
    async with aiofiles.open(file, 'w') as f:
        await f.write(text)
 
async def main(urls):
    tasks = [] 
    for url in urls:
        file = f'{url.split("//")[-1]}.txt'  
        html = await fetch(url)
        tasks.append(write_to_file(file, html))
    await asyncio.gather(*tasks)
 
 # Définir les urls ici
urls = ('','','','')
asyncio.run(main(urls))
